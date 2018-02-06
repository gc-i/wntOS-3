from __future__ import print_function
from __future__ import absolute_import
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_LineCasingDialog import *
from .DamageForm import *
from .DocumentForm import *
from .MaintenanceForm import *
from ..utils.PluginUtils import PluginUtils
from ..model.core_classes import ClIntervalUnit
from ..model.core_classes import ClTypeOfLineCasing, ClNominalWidthOfJacketPipe
from sqlalchemy.exc import SQLAlchemyError
from ..model.DatabaseHelper import *
from qgis.core import QgsFeatureRequest


class LineCasingDialog(QDialog, Ui_LineCasingDialog, DatabaseHelper):

    def __init__(self, layer, feature_id, attr_update=False, parent=None):

        super(LineCasingDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__layer = layer
        self.__feature_id = feature_id
        self.__attr_update = attr_update
        self.__feature = None

        self.installation_date_edit.setDate(QDate.currentDate())
        self.date_of_last_inspection_edit.setDate(QDate.currentDate())

        if not layer.isEditable():
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        try:
            PluginUtils.run_query(PluginUtils.populate_network_cbox, 2, self.network_cbox)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.inspection_intervall_unit_cbox,
                                  ClIntervalUnit, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.casing_type_cbox,
                                  ClTypeOfLineCasing, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.jacket_pipe_diameter_cbox,
                                  ClNominalWidthOfJacketPipe, True)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            return

        request = QgsFeatureRequest().setFilterFid(feature_id)
        try:
            self.__feature = next(layer.getFeatures(request))
        except StopIteration:
            # fix_print_with_import
            print("Feature not found")
            return

        self.damage_form = DamageForm('co_line_casing', self.__feature_id)
        self.tabWidget.addTab(self.damage_form, 'Damages')
        self.maintenance_form = MaintenanceForm('co_line_casing', self.__feature_id)
        self.tabWidget.addTab(self.maintenance_form, 'Maintenance')
        self.document_form = DocumentForm('co_line_casing', self.__feature_id)
        self.tabWidget.addTab(self.document_form, 'Documents')

        if attr_update:
            self.__populate_details()

    def feature_id(self):

        return self.__feature_id

    def __populate_details(self):

        feature = self.__feature

        if feature['line_casing_number']:
            self.line_casing_number_edit.setText(feature['line_casing_number'])
        if feature['length']:
            self.length_sbox.setValue(feature['length'])
        if feature['outer_height']:
            self.outer_height_sbox.setValue(feature['outer_height'])
        if feature['outer_width']:
            self.outer_width_sbox.setValue(feature['outer_width'])
        if feature['installation_date']:
            self.installation_date_edit.setDate(feature['installation_date'])
            self.installation_date_chbox.setChecked(True)
        if feature['inspection_interval']:
            self.inspection_intervall_sbox.setValue(feature['inspection_interval'])
        if feature['inspection_interval_unit']:
            self.inspection_intervall_unit_cbox.\
                setCurrentIndex(self.inspection_intervall_unit_cbox.findData(feature['inspection_interval_unit'], Qt.UserRole))
        if feature['date_of_last_inspection']:
            self.date_of_last_inspection_edit.setDate(feature['date_of_last_inspection'])
            self.date_of_last_inspection_chbox.setChecked(True)
        if feature['casing_type']:
            self.casing_type_cbox.\
                setCurrentIndex(self.casing_type_cbox.findData(feature['casing_type'], Qt.UserRole))
        if feature['jacket_pipe_diameter']:
            self.jacket_pipe_diameter_cbox.setCurrentIndex(self.jacket_pipe_diameter_cbox.findData(feature['jacket_pipe_diameter'], Qt.UserRole))
        if feature['network']:
            self.network_cbox.setCurrentIndex(self.network_cbox.findData(feature['network'], Qt.UserRole))

    @pyqtSlot(int)
    def on_installation_date_chbox_stateChanged(self, state):

        if self.installation_date_chbox.isChecked():
            self.installation_date_edit.setEnabled(True)
        else:
            self.installation_date_edit.setEnabled(False)

    @pyqtSlot(int)
    def on_date_of_last_inspection_chbox_stateChanged(self, state):

        if self.date_of_last_inspection_chbox.isChecked():
            self.date_of_last_inspection_edit.setEnabled(True)
        else:
            self.date_of_last_inspection_edit.setEnabled(False)

    def accept(self):

        if not self.__validate_user_input():
            return

        feature = self.__feature

        self.__layer.beginEditCommand('Update attributes (co_line_casing)')

        attr_val = self.line_casing_number_edit.text() if len(self.line_casing_number_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('line_casing_number'), attr_val)

        attr_val = self.length_sbox.value() if self.length_sbox.value() != 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('length'), attr_val)

        attr_val = self.outer_height_sbox.value() if self.outer_height_sbox.value() != 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('outer_height'), attr_val)

        attr_val = self.outer_width_sbox.value() if self.outer_width_sbox.value() != 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('outer_width'), attr_val)

        attr_val = self.installation_date_edit.date() if self.installation_date_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('installation_date'), attr_val)

        attr_val = self.inspection_intervall_sbox.value() if self.inspection_intervall_sbox.value() > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('inspection_interval'), attr_val)

        attr_val = self.inspection_intervall_unit_cbox.itemData(self.inspection_intervall_unit_cbox.currentIndex(),
                                                                Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('inspection_interval_unit'), attr_val)

        attr_val = self.date_of_last_inspection_edit.date() if self.date_of_last_inspection_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('date_of_last_inspection'), attr_val)

        attr_val = self.casing_type_cbox.itemData(self.casing_type_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('casing_type'), attr_val)

        attr_val = self.jacket_pipe_diameter_cbox.itemData(self.jacket_pipe_diameter_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('jacket_pipe_diameter'), attr_val)

        attr_val = self.network_cbox.itemData(self.network_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('network'), attr_val)

        self.__layer.endEditCommand()

        try:
            PluginUtils.run_query(self.__save_maintenance_and_documents)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        QDialog.accept(self)

    def __save_maintenance_and_documents(self):

        try:
            self.commit()
        except SQLAlchemyError as e:
            raise e

    def __discard_maintenance_and_documents(self):

        self.rollback()

    def reject(self):

        try:
            PluginUtils.run_query(self.__discard_maintenance_and_documents)
        except WntException as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

        QDialog.reject(self)

    def __validate_user_input(self):

        self.line_casing_number_edit.setText(self.line_casing_number_edit.text().strip())

        if self.inspection_intervall_sbox.value() > 0 and self.inspection_intervall_unit_cbox.currentIndex() == 0:
            PluginUtils.show_message(self, self.tr('Missing Interval Unit'),
                                     self.tr('Select the unit for the inspection interval!'))
            return False

        if self.inspection_intervall_sbox.value() == 0 and self.inspection_intervall_unit_cbox.currentIndex() > 0:
            PluginUtils.show_message(self, self.tr('No Inspection Interval'),
                                     self.tr('Set the inspection interval to a value greater than 0!'))
            return False

        # Dates must not be in the "future"
        if self.installation_date_chbox.isChecked() and self.installation_date_edit.date() > QDate.currentDate():
            PluginUtils.show_message(self, self.tr('Future Date'),
                                     self.tr('The installation date must not be in the future!'))
            return False

        return True

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            tab_index = self.tabWidget.currentIndex()
            if tab_index == 0:
                PluginUtils.show_help("Add_Edit_Line_Casing.htm")
            elif tab_index == 1:
                PluginUtils.show_help("Add_Edit_Damage.htm")
            elif tab_index == 2:
                PluginUtils.show_help("Add_Edit_Maintenances.htm")
            elif tab_index == 3:
                PluginUtils.show_help("document_management.html")
