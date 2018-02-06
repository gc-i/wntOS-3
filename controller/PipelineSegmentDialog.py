from __future__ import print_function
from __future__ import absolute_import
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_PipelineSegmentDialog import *
from .DamageForm import *
from .MaintenanceForm import *
from .DocumentForm import *
from ..utils.PluginUtils import PluginUtils
from ..model.core_classes import ClIntervalUnit, ClOperatingState
from ..model.core_classes import ClTypeOfPipelineSegment, ClMaterial, ClTypeOfPlacement, ClPositionalAccuracy
from ..model.core_classes import ClNominalWidthOfPipelineSegment, ClMountingTypeOfPipelineSegment
from sqlalchemy.exc import SQLAlchemyError
from ..model.DatabaseHelper import *
from qgis.core import QgsFeatureRequest


class PipelineSegmentDialog(QDialog, Ui_PipelineSegmentDialog, DatabaseHelper):

    def __init__(self, layer, feature_id, attr_update=False, parent=None):

        super(PipelineSegmentDialog, self).__init__(parent)
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
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.inspection_interval_unit_cbox,
                                  ClIntervalUnit, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.operating_state_cbox,
                                  ClOperatingState, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.pipeline_type_cbox,
                                  ClTypeOfPipelineSegment, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.mounting_type_cbox,
                                  ClMountingTypeOfPipelineSegment, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.material_cbox, ClMaterial, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.placement_type_cbox,
                                  ClTypeOfPlacement, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.nominal_width_cbox,
                                  ClNominalWidthOfPipelineSegment, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.positional_accuracy_cbox,
                                  ClPositionalAccuracy, True)
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

        self.damage_form = DamageForm('co_pipeline_segment', self.__feature_id)
        self.tabWidget.addTab(self.damage_form, 'Damages')
        self.maintenance_form = MaintenanceForm('co_pipeline_segment', self.__feature_id)
        self.tabWidget.addTab(self.maintenance_form, 'Maintenance')
        self.document_form = DocumentForm('co_pipeline_segment', self.__feature_id)
        self.tabWidget.addTab(self.document_form, 'Documents')

        if attr_update:
            self.__populate_details()
        else:
            self.operating_state_cbox.setCurrentIndex(self.operating_state_cbox.findData('OP', Qt.UserRole))

    def feature_id(self):

        return self.__feature_id

    def __populate_details(self):

        feature = self.__feature

        if feature['segment_number']:
            self.segment_no_edit.setText(feature['segment_number'])
        if feature['length']:
            self.length_edit.setText('{:.2f}'.format(feature['length']))
        if feature['installation_date']:
            self.installation_date_edit.setDate(feature['installation_date'])
            self.installation_date_chbox.setChecked(True)
        if feature['inspection_interval']:
            self.inspection_interval_sbox.setValue(feature['inspection_interval'])
        if feature['inspection_interval_unit']:
            self.inspection_interval_unit_cbox.\
                setCurrentIndex(self.inspection_interval_unit_cbox.findData(feature['inspection_interval_unit'], Qt.UserRole))
        if feature['date_of_last_inspection']:
            self.date_of_last_inspection_edit.setDate(feature['date_of_last_inspection'])
            self.date_of_last_inspection_chbox.setChecked(True)
        if feature['operating_state']:
            self.operating_state_cbox.\
                setCurrentIndex(self.operating_state_cbox.findData(feature['operating_state'], Qt.UserRole))
        if feature['date_of_status_change']:
            self.status_change_date_edit.setDate(feature['date_of_status_change'])
            self.status_change_date_chbox.setChecked(True)
        if feature['pipeline_type']:
            self.pipeline_type_cbox.\
                setCurrentIndex(self.pipeline_type_cbox.findData(feature['pipeline_type'], Qt.UserRole))
        if feature['mounting_type']:
            self.mounting_type_cbox.\
                setCurrentIndex(self.mounting_type_cbox.findData(feature['mounting_type'], Qt.UserRole))
        if feature['material']:
            self.material_cbox. \
                setCurrentIndex(self.material_cbox.findData(feature['material'], Qt.UserRole))
        if feature['placement_type']:
            self.placement_type_cbox. \
                setCurrentIndex(self.placement_type_cbox.findData(feature['placement_type'], Qt.UserRole))
        if feature['nominal_width']:
            self.nominal_width_cbox. \
                setCurrentIndex(self.nominal_width_cbox.findData(feature['nominal_width'], Qt.UserRole))
        if feature['positional_accuracy']:
            self.positional_accuracy_cbox. \
                setCurrentIndex(self.positional_accuracy_cbox.findData(feature['positional_accuracy'], Qt.UserRole))
        if feature['outside_diameter']:
            self.outside_diameter_sbox.setValue(feature['outside_diameter'])
        if feature['wall_thickness']:
            self.wall_thickness_sbox.setValue(feature['wall_thickness'])
        if feature['from_height']:
            try:
                height = float(feature['from_height'])
                self.height_at_start_sbox.setValue(height)
            except ValueError:
                pass
        if feature['to_height']:
            try:
                height = float(feature['to_height'])
                self.height_at_end_sbox.setValue(height)
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

        self.__layer.beginEditCommand('Update attributes (co_pipeline_segment)')

        attr_val = self.segment_no_edit.text() if len(self.segment_no_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('segment_number'), attr_val)

        attr_val = self.installation_date_edit.date() if self.installation_date_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('installation_date'), attr_val)

        attr_val = self.inspection_interval_sbox.value() if self.inspection_interval_sbox.value() > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('inspection_interval'), attr_val)

        attr_val = self.inspection_interval_unit_cbox.itemData(self.inspection_interval_unit_cbox.currentIndex(),
                                                                Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('inspection_interval_unit'), attr_val)

        attr_val = self.date_of_last_inspection_edit.date() if self.date_of_last_inspection_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('date_of_last_inspection'), attr_val)

        attr_val = self.operating_state_cbox.itemData(self.operating_state_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('operating_state'), attr_val)

        attr_val = self.status_change_date_edit.date() if self.status_change_date_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('date_of_status_change'), attr_val)

        attr_val = self.pipeline_type_cbox.itemData(self.pipeline_type_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('pipeline_type'), attr_val)

        attr_val = self.mounting_type_cbox.itemData(self.mounting_type_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('mounting_type'), attr_val)

        attr_val = self.material_cbox.itemData(self.material_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('material'), attr_val)

        attr_val = self.placement_type_cbox.itemData(self.placement_type_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('placement_type'), attr_val)

        attr_val = self.nominal_width_cbox.itemData(self.nominal_width_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('nominal_width'), attr_val)

        attr_val = self.positional_accuracy_cbox.itemData(self.positional_accuracy_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('positional_accuracy'), attr_val)

        attr_val = self.outside_diameter_sbox.value()
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('outside_diameter'), attr_val)

        attr_val = self.wall_thickness_sbox.value()
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('wall_thickness'), attr_val)

        attr_val = self.height_at_start_sbox.value()
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('from_height'), attr_val)

        attr_val = self.height_at_end_sbox.value()
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('to_height'), attr_val)

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

        self.segment_no_edit.setText(self.segment_no_edit.text().strip())

        if self.inspection_interval_sbox.value() > 0 and self.inspection_interval_unit_cbox.currentIndex() == 0:
            PluginUtils.show_message(self, self.tr('Missing Interval Unit'),
                                     self.tr('Select the unit for the inspection interval!'))
            return False

        if self.inspection_interval_sbox.value() == 0 and self.inspection_interval_unit_cbox.currentIndex() > 0:
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

        if self.pipeline_type_cbox.currentIndex() == 0:
            PluginUtils.show_message(self, self.tr('No Pipeline Type'),
                                     self.tr('Set the pipeline type!'))
            return False

        return True

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            tab_index = self.tabWidget.currentIndex()
            if tab_index == 0:
                PluginUtils.show_help("Add_Edit_Pipeline_Segment.htm")
            elif tab_index == 1:
                PluginUtils.show_help("Add_Edit_Damage.htm")
            elif tab_index == 2:
                PluginUtils.show_help("Add_Edit_Maintenances.htm")
            elif tab_index == 3:
                PluginUtils.show_help("document_management.html")
