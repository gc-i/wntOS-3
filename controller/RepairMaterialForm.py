from __future__ import absolute_import
from PyQt5.QtWidgets import *
from builtins import range
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_RepairMaterialForm import *
from ..model.core_classes import CoRepairMaterial
from ..model.DatabaseHelper import *
from ..utils.PluginUtils import *
from .RepairMaterialDialog import *


class RepairMaterialForm(QWidget, Ui_RepairMaterialForm, DatabaseHelper):

    def __init__(self, referenced_table_name, referenced_id, parent=None):

        super(RepairMaterialForm, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__referenced_table_name = referenced_table_name
        self.__referenced_id = referenced_id
        try:
            PluginUtils.run_query(self.__populate_material_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.add_material_button.setEnabled(False)
            self.edit_material_button.setEnabled(False)
            self.delete_material_button.setEnabled(False)

    def __populate_material_twidget(self):

        self.material_twidget.clearContents()
        self.material_twidget.setRowCount(0)

        if self.__referenced_table_name == 'co_damage':
            count = self.session.query(CoRepairMaterial).\
                filter(CoRepairMaterial.damage == self.__referenced_id).count()
        else:
            count = self.session.query(CoRepairMaterial).\
                filter(CoRepairMaterial.maintenance == self.__referenced_id).count()

        self.material_twidget.setRowCount(count)

        if self.__referenced_table_name == 'co_damage':
            results = self.session.query(CoRepairMaterial).\
                filter(CoRepairMaterial.damage == self.__referenced_id).all()
        else:
            results = self.session.query(CoRepairMaterial).\
                filter(CoRepairMaterial.maintenance == self.__referenced_id).all()

        i = 0
        for material in results:

            item = QTableWidgetItem('{0}'.format(material.amount))
            item.setData(Qt.UserRole, material.id)
            self.material_twidget.setItem(i, 0, item)

            item = QTableWidgetItem(material.material)
            self.material_twidget.setItem(i, 1, item)

            item = QTableWidgetItem('{:.2f}'.format(material.cost_total_tzs))
            self.material_twidget.setItem(i, 2, item)

            i += 1

        self.material_twidget.resizeColumnsToContents()
        self.material_twidget.horizontalHeader().setStretchLastSection(True)

    @pyqtSlot()
    def on_add_material_button_clicked(self):

        if self.__referenced_id < 0:
            PluginUtils.show_message(self, self.tr("Asset not saved yet"),
                                     self.tr("You must save your changes to database before adding material."))
            return

        dlg = RepairMaterialDialog(None, self.__referenced_id, self.__referenced_table_name, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__reload_and_select_material(dlg.material_id())

    @pyqtSlot()
    def on_edit_material_button_clicked(self):

        if len(self.material_twidget.selectionModel().selectedRows()) == 0:
            return

        for index in self.material_twidget.selectionModel().selectedRows():
            material_id = self.material_twidget.item(index.row(), 0).data(Qt.UserRole)

        dlg = RepairMaterialDialog(material_id, self.__referenced_id, self.__referenced_table_name, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__reload_and_select_material(material_id)

    @pyqtSlot()
    def on_delete_material_button_clicked(self):

        if len(self.material_twidget.selectionModel().selectedRows()) == 0:
            return

        if QMessageBox.No == QMessageBox.question(self, self.tr("Delete Material"),
                                                  self.tr('Delete the selected material?'),
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No):
            return

        for index in self.material_twidget.selectionModel().selectedRows():
            row = index.row()
            material_id = self.material_twidget.item(row, 0).data(Qt.UserRole)

        try:
            PluginUtils.run_query(self.__delete_material, 2, material_id)
            self.material_twidget.removeRow(row)
        except SQLAlchemyError as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

    def __delete_material(self, material_id):

        co_repair_material = self.session.query(CoRepairMaterial).get(material_id)
        self.create_savepoint()
        try:
            self.session.delete(co_repair_material)
            self.release_savepoint()
        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

    def __reload_and_select_material(self, material_id):

        try:
            PluginUtils.run_query(self.__populate_material_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        self.__select_material(material_id)
        self.material_twidget.setFocus()

    def __select_material(self, material_id):

        for row in range(self.material_twidget.rowCount()):
            material_id_2 = self.material_twidget.item(row, 0).data(Qt.UserRole)
            if material_id_2 == material_id:
                self.material_twidget.selectRow(row)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("Add_Edit_Repair_Material.htm")
