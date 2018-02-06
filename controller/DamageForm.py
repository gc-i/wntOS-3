from __future__ import absolute_import
from PyQt5.QtWidgets import *
from builtins import range
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_DamageForm import *
from ..model.DatabaseHelper import *
from ..model.core_classes import CoDamage
from ..utils.PluginUtils import *
from ..utils.LayerUtils import *
from .DamageDialog import *


class DamageForm(QWidget, Ui_DamageForm, DatabaseHelper):

    def __init__(self, damaged_asset_type, damaged_asset_id, parent=None):

        super(DamageForm, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__damaged_asset_id = damaged_asset_id
        self.__damaged_asset_type = damaged_asset_type
        try:
            PluginUtils.run_query(self.__populate_damage_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.edit_damage_button.setEnabled(False)
            self.view_maxcom_button.setEnabled(False)

    def __populate_damage_twidget(self):

        self.damage_twidget.clearContents()
        self.damage_twidget.setRowCount(0)

        count = self.session.query(CoDamage).filter(CoDamage.asset_type == self.__damaged_asset_type).\
            filter(CoDamage.asset_id == self.__damaged_asset_id).count()
        self.damage_twidget.setRowCount(count)

        i = 0
        for co_damage in self.session.query(CoDamage).filter(CoDamage.asset_type == self.__damaged_asset_type).\
            filter(CoDamage.asset_id == self.__damaged_asset_id). \
                order_by(CoDamage.occurrence_timestamp):

            control_no = '' if co_damage.control_no is None else co_damage.control_no
            item = QTableWidgetItem('{}'.format(control_no))
            item.setData(Qt.UserRole, co_damage.id)
            self.damage_twidget.setItem(i, 0, item)

            if co_damage.received_from is not None:
                item = QTableWidgetItem(co_damage.received_from)
                self.damage_twidget.setItem(i, 1, item)

            if co_damage.occurrence_timestamp is not None:
                item = QTableWidgetItem(co_damage.occurrence_timestamp.date().isoformat())
                self.damage_twidget.setItem(i, 2, item)

            if co_damage.registration_timestamp is not None:
                item = QTableWidgetItem(co_damage.registration_timestamp.date().isoformat())
                self.damage_twidget.setItem(i, 3, item)

            if co_damage.repair_timestamp is not None:
                item = QTableWidgetItem(co_damage.repair_timestamp.date().isoformat())
                self.damage_twidget.setItem(i, 4, item)

            if co_damage.repaired_by is not None:
                item = QTableWidgetItem(co_damage.repaired_by)
                self.damage_twidget.setItem(i, 5, item)

            if co_damage.repair_task is not None:
                item = QTableWidgetItem(co_damage.repair_task)
                self.damage_twidget.setItem(i, 6, item)

            if co_damage.cl_damage_type is not None:
                description = co_damage.cl_damage_type.description
                item = QTableWidgetItem(description)
                self.damage_twidget.setItem(i, 7, item)

            if co_damage.cl_damage_cause is not None:
                description = co_damage.cl_damage_cause.description
                item = QTableWidgetItem(description)
                self.damage_twidget.setItem(i, 8, item)

            if co_damage.cl_damage_status is not None:
                description = co_damage.cl_damage_status.description
                item = QTableWidgetItem(description)
                self.damage_twidget.setItem(i, 9, item)

            item = QTableWidgetItem(co_damage.note)
            self.damage_twidget.setItem(i, 10, item)

            i += 1

        self.damage_twidget.resizeColumnsToContents()
        self.damage_twidget.horizontalHeader().setStretchLastSection(True)

    @pyqtSlot()
    def on_view_maxcom_button_clicked(self):

        if len(self.damage_twidget.selectionModel().selectedRows()) == 0:
            return

        for index in self.damage_twidget.selectionModel().selectedRows():
            row = index.row()
            control_no = self.damage_twidget.item(row, 0).text()

        if len(control_no) > 0:
            PluginUtils.open_maxcom(int(control_no), 'COMPLAINT_DAMAGE')

    @pyqtSlot()
    def on_edit_damage_button_clicked(self):

        if len(self.damage_twidget.selectionModel().selectedRows()) == 0:
            return

        for index in self.damage_twidget.selectionModel().selectedRows():
            damage_id = self.damage_twidget.item(index.row(), 0).data(Qt.UserRole)

        layer = LayerUtils.layer_by_data_source('core', 'co_damage')
        dlg = DamageDialog(layer, damage_id, True, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__reload_and_select_damage(damage_id)

    def __reload_and_select_damage(self, damage_id):

        try:
            PluginUtils.run_query(self.__populate_damage_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        self.__select_damage(damage_id)
        self.damage_twidget.setFocus()

    def __select_damage(self, damage_id):

        for row in range(self.damage_twidget.rowCount()):
            damage_id_2 = self.damage_twidget.item(row, 0).data(Qt.UserRole)
            if damage_id_2 == damage_id:
                self.damage_twidget.selectRow(row)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("Add_Edit_Damage.htm")
