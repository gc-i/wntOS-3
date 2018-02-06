from __future__ import absolute_import
from PyQt5.QtWidgets import *
from builtins import range
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_MaintenanceForm import *
from ..model.DatabaseHelper import *
from ..model.core_classes import CoMaintenance
from ..utils.PluginUtils import *
from .MaintenanceDialog import *


class MaintenanceForm(QWidget, Ui_MaintenanceForm, DatabaseHelper):

    def __init__(self, maintained_asset_type, maintained_asset_id, parent=None):

        super(MaintenanceForm, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__maintained_asset_id = maintained_asset_id
        self.__maintained_asset_type = maintained_asset_type
        try:
            PluginUtils.run_query(self.__populate_maintenance_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.add_maintenance_button.setEnabled(False)
            self.edit_maintenance_button.setEnabled(False)
            self.delete_maintenance_button.setEnabled(False)

    def __populate_maintenance_twidget(self):

        self.maintenance_twidget.clearContents()
        self.maintenance_twidget.setRowCount(0)

        count = self.session.query(CoMaintenance).filter(CoMaintenance.asset_type == self.__maintained_asset_type).\
            filter(CoMaintenance.asset_id == self.__maintained_asset_id).count()
        self.maintenance_twidget.setRowCount(count)

        i = 0
        for co_maintenance in self.session.query(CoMaintenance). \
                filter(CoMaintenance.asset_type == self.__maintained_asset_type). \
                filter(CoMaintenance.asset_id == self.__maintained_asset_id). \
                order_by(CoMaintenance.maintenance_timestamp):

            maintenance_date = '' if co_maintenance.maintenance_timestamp is None \
                else co_maintenance.maintenance_timestamp.date().isoformat()
            item = QTableWidgetItem(maintenance_date)
            item.setData(Qt.UserRole, co_maintenance.id)
            self.maintenance_twidget.setItem(i, 0, item)

            if co_maintenance.maintained_by is not None:
                item = QTableWidgetItem(co_maintenance.maintained_by)
                self.maintenance_twidget.setItem(i, 1, item)

            if co_maintenance.maintenance_task is not None:
                item = QTableWidgetItem(co_maintenance.maintenance_task)
                self.maintenance_twidget.setItem(i, 2, item)

            item = QTableWidgetItem(co_maintenance.note)
            self.maintenance_twidget.setItem(i, 3, item)

            i += 1

        self.maintenance_twidget.resizeColumnsToContents()
        self.maintenance_twidget.horizontalHeader().setStretchLastSection(True)

    @pyqtSlot()
    def on_add_maintenance_button_clicked(self):

        if self.__maintained_asset_id < 0:
            PluginUtils.show_message(self, self.tr("Asset not saved yet"),
                                     self.tr("You must save your changes to database before adding a maintenance."))
            return

        dlg = MaintenanceDialog(None, self.__maintained_asset_id, self.__maintained_asset_type, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__reload_and_select_maintenance(dlg.maintenance_id())

    @pyqtSlot()
    def on_edit_maintenance_button_clicked(self):

        if len(self.maintenance_twidget.selectionModel().selectedRows()) == 0:
            return

        for index in self.maintenance_twidget.selectionModel().selectedRows():
            maintenance_id = self.maintenance_twidget.item(index.row(), 0).data(Qt.UserRole)

        dlg = MaintenanceDialog(maintenance_id, self.__maintained_asset_id, self.__maintained_asset_type, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__reload_and_select_maintenance(maintenance_id)

    @pyqtSlot()
    def on_delete_maintenance_button_clicked(self):

        if len(self.maintenance_twidget.selectionModel().selectedRows()) == 0:
            return

        if QMessageBox.No == QMessageBox.question(self, self.tr("Delete Maintenance"),
                                                  self.tr('Delete the selected maintenance?'),
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No):
            return

        for index in self.maintenance_twidget.selectionModel().selectedRows():
            row = index.row()
            maintenance_id = self.maintenance_twidget.item(row, 0).data(Qt.UserRole)

        try:
            PluginUtils.run_query(self.__delete_maintenance, 2, maintenance_id)
            self.maintenance_twidget.removeRow(row)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

    def __delete_maintenance(self, maintenance_id):

        co_maintenance = self.session.query(CoMaintenance).get(maintenance_id)
        self.create_savepoint()
        try:
            self.session.delete(co_maintenance)
            self.release_savepoint()
        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

    def __reload_and_select_maintenance(self, maintenance_id):

        try:
            PluginUtils.run_query(self.__populate_maintenance_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        self.__select_maintenance(maintenance_id)
        self.maintenance_twidget.setFocus()

    def __select_maintenance(self, maintenance_id):

        for row in range(self.maintenance_twidget.rowCount()):
            maintenance_id_2 = self.maintenance_twidget.item(row, 0).data(Qt.UserRole)
            if maintenance_id_2 == maintenance_id:
                self.maintenance_twidget.selectRow(row)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("Add_Edit_Maintenances.htm")
