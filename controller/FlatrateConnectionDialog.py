from __future__ import print_function
from __future__ import absolute_import
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_FlatrateConnectionDialog import *
from .DamageForm import *
from .MaintenanceForm import *
from .CustomerManagementForm import *
from .DocumentForm import *
from ..utils.PluginUtils import PluginUtils
from ..model.core_classes import ClIntervalUnit, ClOperatingState
from ..model.core_classes import CoFlatrateConnection
from sqlalchemy.exc import SQLAlchemyError
from ..model.DatabaseHelper import *
from qgis.core import QgsFeatureRequest


class FlatrateConnectionDialog(QDialog, Ui_FlatrateConnectionDialog, DatabaseHelper):

    def __init__(self, layer, feature_id, attr_update=False, parent=None):

        super(FlatrateConnectionDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__layer = layer
        self.__feature_id = feature_id
        self.__attr_update = attr_update
        self.__feature = None

        self.installation_date_edit.setDate(QDate.currentDate())
        self.status_change_date_edit.setDate(QDate.currentDate())
        self.date_of_first_use_edit.setDate(QDate.currentDate())
        self.date_of_last_inspection_edit.setDate(QDate.currentDate())

        if not layer.isEditable():
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        try:
            PluginUtils.run_query(PluginUtils.populate_network_cbox, 2, self.network_cbox)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.inspection_intervall_unit_cbox,
                                  ClIntervalUnit, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.operating_state_cbox,
                                  ClOperatingState, True)
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

        self.damage_form = DamageForm('co_flatrate_connection', self.__feature_id)
        self.tabWidget.addTab(self.damage_form, 'Damages')
        self.maintenance_form = MaintenanceForm('co_flatrate_connection', self.__feature_id)
        self.tabWidget.addTab(self.maintenance_form, 'Maintenance')
        self.document_form = DocumentForm('co_flatrate_connection', self.__feature_id)
        self.tabWidget.addTab(self.document_form, 'Documents')
        self.customer_form = CustomerManagementForm(CoFlatrateConnection, self.__feature_id)
        self.tabWidget.addTab(self.customer_form, 'Customer')

        if attr_update:
            self.__populate_details()
        else:
            self.operating_state_cbox.setCurrentIndex(self.operating_state_cbox.findData('OP', Qt.UserRole))

    def feature_id(self):

        return self.__feature_id

    def __populate_details(self):

        feature = self.__feature

        if feature['connection_number']:
            self.connection_no_edit.setText(feature['connection_number'])
        if feature['control_no']:
            self.control_no_sbox.setValue(feature['control_no'])
        if feature['plot_no']:
            self.plot_no_edit.setText(feature['plot_no'])
        if feature['district']:
            self.district_edit.setText(feature['district'])
        if feature['zone']:
            self.zone_edit.setText(feature['zone'])
        if feature['ward']:
            self.ward_edit.setText(feature['ward'])
        if feature['street']:
            self.street_edit.setText(feature['street'])
        if feature['installation_date']:
            self.installation_date_edit.setDate(feature['installation_date'])
            self.installation_date_chbox.setChecked(True)
        if feature['date_of_first_use']:
            self.date_of_first_use_edit.setDate(feature['date_of_first_use'])
            self.date_of_first_use_chbox.setChecked(True)
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

    @pyqtSlot(int)
    def on_date_of_first_use_chbox_stateChanged(self, state):

        if self.date_of_first_use_chbox.isChecked():
            self.date_of_first_use_edit.setEnabled(True)
        else:
            self.date_of_first_use_edit.setEnabled(False)

    def accept(self):

        if not self.__validate_user_input():
            return

        feature = self.__feature

        self.__layer.beginEditCommand('Update attributes (co_flatrate_connection)')

        attr_val = self.connection_no_edit.text() if len(self.connection_no_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('connection_number'), attr_val)

        attr_val = self.control_no_sbox.value() if self.control_no_sbox.value() > -1 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('control_no'), attr_val)

        attr_val = self.plot_no_edit.text() if len(self.plot_no_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('plot_no'), attr_val)

        attr_val = self.district_edit.text() if len(self.district_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('district'), attr_val)

        attr_val = self.zone_edit.text() if len(self.zone_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('zone'), attr_val)

        attr_val = self.ward_edit.text() if len(self.ward_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('ward'), attr_val)

        attr_val = self.street_edit.text() if len(self.street_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('street'), attr_val)

        attr_val = self.installation_date_edit.date() if self.installation_date_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('installation_date'), attr_val)

        attr_val = self.date_of_first_use_edit.date() if self.date_of_first_use_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('date_of_first_use'), attr_val)

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

        self.connection_no_edit.setText(self.connection_no_edit.text().strip())

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

        return True

    @pyqtSlot()
    def on_verify_button_clicked(self):

        control_no = self.control_no_sbox.value()

        count = self.session.query(MxApplication).filter(MxApplication.id == control_no).count()
        if count == 0:
            PluginUtils.show_error(self, self.tr('Verifying Control Number'),
                                     self.tr('Failure: control number not found in MAXCOM database!'))
        else:
            PluginUtils.show_message(self, self.tr('Verifying Control Number'),
                                     self.tr('Success: control number found in MAXCOM database!'))

    @pyqtSlot()
    def on_view_maxcom_button_clicked(self):

        control_no = self.control_no_sbox.value()
        if control_no > -1:
            PluginUtils.open_maxcom(control_no, 'NEW')

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            tab_index = self.tabWidget.currentIndex()
            if tab_index == 0:
                PluginUtils.show_help("Add_Edit_Flatrate_Connection.htm")
            elif tab_index == 1:
                PluginUtils.show_help("Add_Edit_Damage.htm")
            elif tab_index == 2:
                PluginUtils.show_help("Add_Edit_Maintenances.htm")
            elif tab_index == 3:
                PluginUtils.show_help("document_management.html")
            elif tab_index == 4:
                PluginUtils.show_help("Manage_Customer.htm")
