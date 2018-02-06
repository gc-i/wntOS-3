from __future__ import print_function
from __future__ import absolute_import
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_UtilityStationDialog import *
from .DamageForm import *
from .MaintenanceForm import *
from .DocumentForm import *
from ..utils.PluginUtils import PluginUtils
from ..model.core_classes import ClOperatingState
from ..model.core_classes import ClCapacityUnit, ClTypeOfStation, ClPurposeOfStation, ClLocation
from sqlalchemy.exc import SQLAlchemyError
from ..model.DatabaseHelper import *
from qgis.core import QgsFeatureRequest


class UtilityStationDialog(QDialog, Ui_UtilityStationDialog, DatabaseHelper):

    def __init__(self, layer, feature_id, attr_update=False, parent=None):

        super(UtilityStationDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__layer = layer
        self.__feature_id = feature_id
        self.__attr_update = attr_update
        self.__feature = None

        self.status_change_date_edit.setDate(QDate.currentDate())

        if not layer.isEditable():
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        try:
            PluginUtils.run_query(PluginUtils.populate_network_cbox, 2, self.network_cbox)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.purpose_cbox, ClPurposeOfStation, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.station_type_cbox, ClTypeOfStation, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.capacity_unit_cbox, ClCapacityUnit, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.operating_state_cbox,
                                  ClOperatingState, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.location_cbox, ClLocation, True)

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

        self.damage_form = DamageForm('co_utility_station', self.__feature_id)
        self.tabWidget.addTab(self.damage_form, 'Damages')
        self.maintenance_form = MaintenanceForm('co_utility_station', self.__feature_id)
        self.tabWidget.addTab(self.maintenance_form, 'Maintenance')
        self.document_form = DocumentForm('co_utility_station', self.__feature_id)
        self.tabWidget.addTab(self.document_form, 'Documents')

        if attr_update:
            self.__populate_details()
        else:
            self.operating_state_cbox.setCurrentIndex(self.operating_state_cbox.findData('OP', Qt.UserRole))

    def feature_id(self):

        return self.__feature_id

    def __populate_details(self):

        feature = self.__feature

        if feature['station_number']:
            self.station_number_edit.setText(feature['station_number'])
        if feature['station_name']:
            self.station_name_edit.setText(feature['station_name'])
        if feature['installation_year']:
            self.installation_year_sbox.setValue(feature['installation_year'])
        if feature['capacity']:
            self.capacity_sbox.setValue(feature['capacity'])
        if feature['capacity_unit']:
            self.capacity_unit_cbox.setCurrentIndex(self.capacity_unit_cbox.findData(feature['capacity_unit'], Qt.UserRole))
        if feature['operating_state']:
            self.operating_state_cbox.\
                setCurrentIndex(self.operating_state_cbox.findData(feature['operating_state'], Qt.UserRole))
        if feature['date_of_status_change']:
            self.status_change_date_edit.setDate(feature['date_of_status_change'])
            self.status_change_date_chbox.setChecked(True)
        if feature['location']:
            self.location_cbox. \
                setCurrentIndex(self.location_cbox.findData(feature['location'], Qt.UserRole))
        if feature['station_type']:
            self.station_type_cbox.\
                setCurrentIndex(self.station_type_cbox.findData(feature['station_type'], Qt.UserRole))
        if feature['purpose']:
            self.purpose_cbox.\
                setCurrentIndex(self.purpose_cbox.findData(feature['purpose'], Qt.UserRole))
        if feature['height']:
            try:
                height = float(feature['height'])
                self.height_sbox.setValue(height)
            except ValueError:
                pass
        if feature['network']:
            self.network_cbox.setCurrentIndex(self.network_cbox.findData(feature['network'], Qt.UserRole))


    @pyqtSlot(int)
    def on_status_change_date_chbox_stateChanged(self, state):

        if self.status_change_date_chbox.isChecked():
            self.status_change_date_edit.setEnabled(True)
        else:
            self.status_change_date_edit.setEnabled(False)

    def accept(self):

        if not self.__validate_user_input():
            return

        feature = self.__feature

        self.__layer.beginEditCommand('Update attributes (co_utility_station)')

        attr_val = self.station_number_edit.text() if len(self.station_number_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('station_number'), attr_val)

        attr_val = self.station_name_edit.text() if len(self.station_name_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('station_name'), attr_val)

        attr_val = self.installation_year_sbox.value() if self.installation_year_sbox.value() > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('installation_year'), attr_val)

        attr_val = self.capacity_sbox.value() if self.capacity_sbox.value() > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('capacity'), attr_val)

        attr_val = self.capacity_unit_cbox.itemData(self.capacity_unit_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('capacity_unit'), attr_val)

        attr_val = self.operating_state_cbox.itemData(self.operating_state_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('operating_state'), attr_val)

        attr_val = self.status_change_date_edit.date() if self.status_change_date_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('date_of_status_change'), attr_val)

        attr_val = self.location_cbox.itemData(self.location_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('location'), attr_val)

        attr_val = self.station_type_cbox.itemData(self.station_type_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('station_type'), attr_val)

        attr_val = self.purpose_cbox.itemData(self.purpose_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('purpose'), attr_val)

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

        self.station_number_edit.setText(self.station_number_edit.text().strip())

        # Dates must not be in the "future"
        if self.status_change_date_chbox.isChecked() and self.status_change_date_edit.date() > QDate.currentDate():
            PluginUtils.show_message(self, self.tr('Future Date'),
                                     self.tr('The date of status change must not be in the future!'))
            return False

        if self.station_type_cbox.currentIndex() == 0:
            PluginUtils.show_message(self, self.tr('No Station Type'),
                                     self.tr('Set the station type!'))
            return False

        return True

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            tab_index = self.tabWidget.currentIndex()
            if tab_index == 0:
                PluginUtils.show_help("Add_Edit_Utility_Station.htm")
            elif tab_index == 1:
                PluginUtils.show_help("Add_Edit_Damage.htm")
            elif tab_index == 2:
                PluginUtils.show_help("Add_Edit_Maintenances.htm")
            elif tab_index == 3:
                PluginUtils.show_help("document_management.html")
