from __future__ import absolute_import
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_MaintenanceDialog import *
from .RepairMaterialForm import *
from ..utils.PluginUtils import PluginUtils
from ..model.core_classes import CoMaintenance
from sqlalchemy.exc import SQLAlchemyError
from ..model.DatabaseHelper import *


class MaintenanceDialog(QDialog, Ui_MaintenanceDialog, DatabaseHelper):

    def __init__(self, maintenance_id, maintained_asset_id, maintained_asset_type, parent=None):

        super(MaintenanceDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__maintenance_id = maintenance_id
        self.__maintained_asset_id = maintained_asset_id
        self.__maintained_asset_type = maintained_asset_type

        self.maintenance_date_edit.setDate(QDate.currentDate())

        try:
            PluginUtils.run_query(self.__populate_maintained_by_cbox)
            PluginUtils.run_query(self.__populate_maintenance_task_cbox)

            self.create_savepoint()

            if maintenance_id is None:
                co_maintenance = CoMaintenance()
                co_maintenance.maintenance_task = 'XXX'
                co_maintenance.maintained_by = 'XXX'
                co_maintenance.maintenance_timestamp = '1992-01-01'
                self.session.add(co_maintenance)
                self.session.flush()
                self.__maintenance_id = co_maintenance.id

            else:
                PluginUtils.run_query(self.__populate_maintenance_details)

        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        self.material_form = RepairMaterialForm('CoMaintenance', self.__maintenance_id)
        self.tabWidget.addTab(self.material_form, 'Repair Material')

    def maintenance_id(self):

        return self.__maintenance_id

    def __populate_maintained_by_cbox(self):

        for maintained_by, in self.session.query(CoMaintenance.maintained_by.distinct()).\
                order_by(CoMaintenance.maintained_by):
            self.maintained_by_cbox.addItem(maintained_by)

        self.maintained_by_cbox.setCurrentIndex(-1)

    def __populate_maintenance_task_cbox(self):

        for maintenance_task, in self.session.query(CoMaintenance.maintenance_task.distinct()).\
                order_by(CoMaintenance.maintenance_task):
            self.maintenance_task_cbox.addItem(maintenance_task)

        self.maintenance_task_cbox.setCurrentIndex(-1)

    def __populate_maintenance_details(self):

        co_maintenance = self.session.query(CoMaintenance).get(self.__maintenance_id)

        self.maintenance_date_edit.setDate(co_maintenance.maintenance_timestamp)
        self.maintained_by_cbox.setCurrentIndex(self.maintained_by_cbox.findText(co_maintenance.maintained_by))
        self.maintenance_task_cbox.setCurrentIndex(self.maintenance_task_cbox.findText(co_maintenance.maintenance_task))
        self.note_edit.setPlainText(co_maintenance.note)

    def accept(self):

        if not self.__validate_user_input():
            return

        try:
            PluginUtils.run_query(self.__save_maintenance)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        QDialog.accept(self)

    def __save_maintenance(self):

        maintenance_date = PluginUtils.convert_qt_date_to_python(self.maintenance_date_edit.date())
        maintained_by = self.maintained_by_cbox.lineEdit().text() \
            if len(self.maintained_by_cbox.lineEdit().text()) > 0 else None
        maintenance_task = self.maintenance_task_cbox.lineEdit().text() \
            if len(self.maintenance_task_cbox.lineEdit().text()) > 0 else None
        note = self.note_edit.toPlainText() if len(self.note_edit.toPlainText()) > 0 else None

        self.create_savepoint()
        try:
            co_maintenance = self.session.query(CoMaintenance).get(self.__maintenance_id)
            co_maintenance.maintenance_timestamp = maintenance_date
            co_maintenance.maintained_by = maintained_by
            co_maintenance.maintenance_task = maintenance_task
            co_maintenance.asset_type = self.__maintained_asset_type
            co_maintenance.asset_id = self.__maintained_asset_id
            co_maintenance.note = note
            self.session.add(co_maintenance)
            self.release_savepoint()

        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

    def __discard_maintenance(self):

        self.rollback_to_savepoint()

    def reject(self):

        try:
            PluginUtils.run_query(self.__discard_maintenance)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

        QDialog.reject(self)

    def __validate_user_input(self):

        self.maintained_by_cbox.lineEdit().setText(self.maintained_by_cbox.lineEdit().text().strip())
        self.maintenance_task_cbox.lineEdit().setText(self.maintenance_task_cbox.lineEdit().text().strip())
        self.note_edit.setPlainText(self.note_edit.toPlainText().strip())

        if len(self.maintenance_task_cbox.lineEdit().text()) == 0:
            PluginUtils.show_message(self, self.tr('No Maintenance Task'),
                                     self.tr('Please provide the task regarding the maintenance!'))
            return False

        if self.maintenance_date_edit.date() > QDate.currentDate():
            PluginUtils.show_message(self, self.tr('Future Date'),
                                     self.tr('The maintenance date must not be in the future!'))
            return False

        if len(self.maintained_by_cbox.lineEdit().text()) == 0:
            PluginUtils.show_message(self, self.tr('No Maintained By'),
                                     self.tr('Please provide the person conducting the maintenance!'))
            return False

        return True

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            tab_index = self.tabWidget.currentIndex()
            if tab_index == 0:
                PluginUtils.show_help("Add_Edit_Maintenances.htm")
            elif tab_index == 1:
                PluginUtils.show_help("Add_Edit_Repair_Material.htm")


