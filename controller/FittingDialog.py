from __future__ import print_function
from __future__ import absolute_import
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_FittingDialog import *
from .DamageForm import *
from .MaintenanceForm import *
from .DocumentForm import *
from ..utils.PluginUtils import PluginUtils
from ..model.core_classes import ClIntervalUnit, ClOperatingState, ClSwitchingState
from ..model.core_classes import ClMountingTypeOfFitting, ClTypeOfFitting, ClPurposeOfFitting, ClNominalWidthOfFitting
from sqlalchemy.exc import SQLAlchemyError
from ..model.DatabaseHelper import *
from qgis.core import QgsFeatureRequest


class FittingDialog(QDialog, Ui_FittingDialog, DatabaseHelper):

    def __init__(self, layer, feature_id, attr_update=False, parent=None):

        super(FittingDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__layer = layer
        self.__feature_id = feature_id
        self.__attr_update = attr_update
        self.__feature = None

        self.installation_date_edit.setDate(QDate.currentDate())
        self.status_change_date_edit.setDate(QDate.currentDate())
        self.date_of_last_inspection_edit.setDate(QDate.currentDate())

        if not layer.isEditable():
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        try:
            PluginUtils.run_query(PluginUtils.populate_network_cbox, 2, self.network_cbox)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.inspection_intervall_unit_cbox,
                                  ClIntervalUnit, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.operating_state_cbox,
                                  ClOperatingState, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.switching_state_cbox,
                                  ClSwitchingState, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.mounting_type_cbox,
                                  ClMountingTypeOfFitting, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.fitting_type_cbox,
                                  ClTypeOfFitting, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.fitting_purpose_cbox,
                                  ClPurposeOfFitting, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.nominal_width_cbox,
                                  ClNominalWidthOfFitting, True)
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

        self.damage_form = DamageForm('co_fitting', self.__feature_id)
        self.tabWidget.addTab(self.damage_form, 'Damages')
        self.maintenance_form = MaintenanceForm('co_fitting', self.__feature_id)
        self.tabWidget.addTab(self.maintenance_form, 'Maintenance')
        self.document_form = DocumentForm('co_fitting', self.__feature_id)
        self.tabWidget.addTab(self.document_form, 'Documents')

        if attr_update:
            self.__populate_details()
        else:
            self.operating_state_cbox.setCurrentIndex(self.operating_state_cbox.findData('OP', Qt.UserRole))

    def feature_id(self):

        return self.__feature_id

    def __populate_details(self):

        feature = self.__feature

        if feature['fitting_number']:
            self.fitting_no_edit.setText(feature['fitting_number'])
        if feature['installation_length']:
            self.installation_length_sbox.setValue(feature['installation_length'])
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
        if feature['operating_state']:
            self.operating_state_cbox.\
                setCurrentIndex(self.operating_state_cbox.findData(feature['operating_state'], Qt.UserRole))
        if feature['date_of_status_change']:
            self.status_change_date_edit.setDate(feature['date_of_status_change'])
            self.status_change_date_chbox.setChecked(True)
        if feature['switching_state']:
            self.switching_state_cbox.\
                setCurrentIndex(self.switching_state_cbox.findData(feature['switching_state'], Qt.UserRole))
        if feature['mounting_type']:
            self.mounting_type_cbox.\
                setCurrentIndex(self.mounting_type_cbox.findData(feature['mounting_type'], Qt.UserRole))
        if feature['fitting_type']:
            self.fitting_type_cbox. \
                setCurrentIndex(self.fitting_type_cbox.findData(feature['fitting_type'], Qt.UserRole))
        if feature['fitting_purpose']:
            self.fitting_purpose_cbox. \
                setCurrentIndex(self.fitting_purpose_cbox.findData(feature['fitting_purpose'], Qt.UserRole))
        if feature['nominal_width']:
            self.nominal_width_cbox. \
                setCurrentIndex(self.nominal_width_cbox.findData(feature['nominal_width'], Qt.UserRole))
        if feature['height']:
            try:
                height = float(feature['height'])
                self.height_sbox.setValue(height)
            except ValueError:
                pass
        if feature['network']:
            self.network_cbox.setCurrentIndex(self.network_cbox.findData(feature['network'], Qt.UserRole))

    @pyqtSlot(int)
    def on_installation_date_chbox_stateChanged(self, state):

        if self.installation_date_chbox.isChecked():
            self.installation_date_edit.setEnabled(True)
        else:
            self.installation_date_edit.setEnabled(False)

    @pyqtSlot(int)
    def on_status_change_date_chbox_stateChanged(self, state):

        if self.status_change_date_chbox.isChecked():
            self.status_change_date_edit.setEnabled(True)
        else:
            self.status_change_date_edit.setEnabled(False)

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

        self.__layer.beginEditCommand('Update attributes (co_fitting)')

        attr_val = self.fitting_no_edit.text() if len(self.fitting_no_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('fitting_number'), attr_val)

        attr_val = self.installation_length_sbox.value() if self.installation_length_sbox.value() != 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('installation_length'), attr_val)

        attr_val = self.installation_date_edit.date() if self.installation_date_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('installation_date'), attr_val)

        attr_val = self.inspection_intervall_sbox.value() if self.inspection_intervall_sbox.value() > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('inspection_interval'), attr_val)

        attr_val = self.inspection_intervall_unit_cbox.itemData(self.inspection_intervall_unit_cbox.currentIndex(),
                                                                Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('inspection_interval_unit'), attr_val)

        attr_val = self.date_of_last_inspection_edit.date() if self.date_of_last_inspection_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('date_of_last_inspection'), attr_val)

        attr_val = self.operating_state_cbox.itemData(self.operating_state_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('operating_state'), attr_val)

        attr_val = self.status_change_date_edit.date() if self.status_change_date_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('date_of_status_change'), attr_val)

        attr_val = self.switching_state_cbox.itemData(self.switching_state_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('switching_state'), attr_val)

        attr_val = self.mounting_type_cbox.itemData(self.mounting_type_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('mounting_type'), attr_val)

        attr_val = self.fitting_type_cbox.itemData(self.fitting_type_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('fitting_type'), attr_val)

        attr_val = self.fitting_purpose_cbox.itemData(self.fitting_purpose_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('fitting_purpose'), attr_val)

        attr_val = self.nominal_width_cbox.itemData(self.nominal_width_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('nominal_width'), attr_val)

        attr_val = self.height_sbox.value()
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('height'), attr_val)

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

        self.fitting_no_edit.setText(self.fitting_no_edit.text().strip())

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

        if self.status_change_date_chbox.isChecked() and self.status_change_date_edit.date() > QDate.currentDate():
            PluginUtils.show_message(self, self.tr('Future Date'),
                                     self.tr('The date of status change must not be in the future!'))
            return False

        if self.date_of_last_inspection_chbox.isChecked() and self.date_of_last_inspection_edit.date() > QDate.currentDate():
            PluginUtils.show_message(self, self.tr('Future Date'),
                                     self.tr('The date of last inspection must not be in the future!'))
            return False

        if self.fitting_type_cbox.currentIndex() == 0:
            PluginUtils.show_message(self, self.tr('No Fitting Type'),
                                     self.tr('Set the fitting type!'))
            return False

        return True

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            tab_index = self.tabWidget.currentIndex()
            if tab_index == 0:
                PluginUtils.show_help("Add_Edit_Fitting.htm")
            elif tab_index == 1:
                PluginUtils.show_help("Add_Edit_Damage.htm")
            elif tab_index == 2:
                PluginUtils.show_help("Add_Edit_Maintenances.htm")
            elif tab_index == 3:
                PluginUtils.show_help("document_management.html")

    @pyqtSlot(int)
    def on_fitting_type_cbox_currentIndexChanged(self, index):

        if self.fitting_type_cbox.itemData(index, Qt.UserRole) == 'FH' \
                or self.fitting_type_cbox.itemData(index, Qt.UserRole) is None:

            self.fitting_purpose_cbox.setCurrentIndex(0)
            self.fitting_purpose_cbox.setEnabled(False)
        else:
            self.fitting_purpose_cbox.setEnabled(True)

