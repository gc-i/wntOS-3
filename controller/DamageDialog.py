from __future__ import print_function
from __future__ import absolute_import
from PyQt5.QtWidgets import *
from builtins import range
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_DamageDialog import *
from .DocumentForm import *
from .RepairMaterialForm import *
from ..utils.PluginUtils import PluginUtils
from ..model.core_classes import ClDamageType, ClDamageCause, ClDamageStatus
from ..model.core_classes import CoDamage, MxWaterLeakageComplaint
from sqlalchemy.exc import SQLAlchemyError
from ..model.DatabaseHelper import *
from qgis.core import QgsFeatureRequest


class DamageDialog(QDialog, Ui_DamageDialog, DatabaseHelper):

    def __init__(self, layer, feature_id, attr_update=False, parent=None):

        super(DamageDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__layer = layer
        self.__feature_id = feature_id
        self.__attr_update = attr_update
        self.__feature = None
        self.__nearby_features = []
        self.__set_asset_type = None
        self.__set_asset_id = None

        self.occurrence_date_edit.setDate(QDate.currentDate())
        self.registration_date_edit.setDate(QDate.currentDate())
        self.repair_date_edit.setDate(QDate.currentDate())

        if not layer.isEditable():
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        try:
            PluginUtils.run_query(PluginUtils.populate_network_cbox, 2, self.network_cbox)
            PluginUtils.run_query(self.__populate_received_from_cbox)
            PluginUtils.run_query(self.__populate_repaired_by_cbox)
            PluginUtils.run_query(self.__populate_repair_task_cbox)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.type_cbox, ClDamageType, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.cause_cbox, ClDamageCause, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.status_cbox, ClDamageStatus, True)
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

        self.document_form = DocumentForm('co_damage', self.__feature_id)
        self.tabWidget.addTab(self.document_form, 'Documents')

        self.material_form = RepairMaterialForm('co_damage', self.__feature_id)
        self.tabWidget.addTab(self.material_form, 'Repair Material')

        self.__populate_nearby_features()

        self.warning_label.clear()

        if attr_update:
            self.__populate_details()
        else:
            self.status_cbox.setCurrentIndex(1)

    def __populate_received_from_cbox(self):

        for received_from, in self.session.query(CoDamage.received_from.distinct()).order_by(CoDamage.received_from):
            self.received_from_cbox.addItem(received_from)

        self.received_from_cbox.setCurrentIndex(-1)

    def __populate_repaired_by_cbox(self):

        for repaired_by, in self.session.query(CoDamage.repaired_by.distinct()).order_by(CoDamage.repaired_by):
            self.repaired_by_cbox.addItem(repaired_by)

        self.repaired_by_cbox.setCurrentIndex(-1)

    def __populate_repair_task_cbox(self):

        for repair_task, in self.session.query(CoDamage.repair_task.distinct()).order_by(CoDamage.repair_task):
            self.repair_task_cbox.addItem(repair_task)

        self.repair_task_cbox.setCurrentIndex(-1)

    def __populate_details(self):

        feature = self.__feature

        if feature['control_no']:
            self.control_no_sbox.setValue(feature['control_no'])
        if feature['occurrence_timestamp']:
            self.occurrence_date_edit.setDate(feature['occurrence_timestamp'].date())
            self.occurrence_date_chbox.setChecked(True)
        self.registration_date_edit.setDate(feature['registration_timestamp'].date())
        if feature['repair_timestamp']:
            self.repair_date_edit.setDate(feature['repair_timestamp'].date())
            self.repair_date_chbox.setChecked(True)

        if feature['received_from']:
            self.received_from_cbox.setCurrentIndex(self.received_from_cbox.findText(feature['received_from']))
        if feature['repaired_by']:
            self.repaired_by_cbox.setCurrentIndex(self.repaired_by_cbox.findText(feature['repaired_by']))
        if feature['repair_task']:
            self.repair_task_cbox.setCurrentIndex(self.repair_task_cbox.findText(feature['repair_task']))

        if feature['damage_type']:
            self.type_cbox.setCurrentIndex(self.type_cbox.findData(feature['damage_type'], Qt.UserRole))

        if feature['damage_cause']:
            self.cause_cbox.setCurrentIndex(self.cause_cbox.findData(feature['damage_cause'], Qt.UserRole))

        if feature['damage_status']:
            self.status_cbox.setCurrentIndex(self.status_cbox.findData(feature['damage_status'], Qt.UserRole))

        if feature['buffer']:
            self.buffer_sbox.setValue(feature['buffer'])

        if feature['note']:
            self.note_edit.setPlainText(feature['note'])

        if feature['asset_type']:
            self.__highlight_row(feature['asset_type'], feature['asset_id'])

        if feature['height']:
            try:
                height = float(feature['height'])
                self.height_sbox.setValue(height)
            except ValueError:
                pass

        if feature['network']:
            self.network_cbox.setCurrentIndex(self.network_cbox.findData(feature['network'], Qt.UserRole))

    @pyqtSlot(int)
    def on_occurrence_date_chbox_stateChanged(self, state):

        if self.occurrence_date_chbox.isChecked():
            self.occurrence_date_edit.setEnabled(True)
        else:
            self.occurrence_date_edit.setEnabled(False)

    @pyqtSlot(int)
    def on_repair_date_chbox_stateChanged(self, state):

        if self.repair_date_chbox.isChecked():
            self.repair_date_edit.setEnabled(True)
        else:
            self.repair_date_edit.setEnabled(False)

    def accept(self):

        if not self.__validate_user_input():
            return

        feature = self.__feature

        self.__layer.beginEditCommand('Update attributes (co_damage)')

        attr_val = self.control_no_sbox.value() if self.control_no_sbox.value() > -1 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('control_no'), attr_val)

        attr_val = self.occurrence_date_edit.dateTime() if self.occurrence_date_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('occurrence_timestamp'), attr_val)

        attr_val = self.received_from_cbox.lineEdit().text() \
            if len(self.received_from_cbox.lineEdit().text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('received_from'), attr_val)

        attr_val = self.registration_date_edit.dateTime()
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('registration_timestamp'), attr_val)

        attr_val = self.repair_date_edit.dateTime() if self.repair_date_chbox.isChecked() else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('repair_timestamp'), attr_val)

        attr_val = self.repaired_by_cbox.lineEdit().text() \
            if len(self.repaired_by_cbox.lineEdit().text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('repaired_by'), attr_val)

        attr_val = self.repair_task_cbox.lineEdit().text() \
            if len(self.repair_task_cbox.lineEdit().text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('repair_task'), attr_val)

        attr_val = self.type_cbox.itemData(self.type_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('damage_type'), attr_val)

        attr_val = self.cause_cbox.itemData(self.cause_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('damage_cause'), attr_val)

        attr_val = self.status_cbox.itemData(self.status_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('damage_status'), attr_val)

        attr_val = self.buffer_sbox.value()
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('buffer'), attr_val)

        attr_val = self.note_edit.toPlainText() if len(self.note_edit.toPlainText()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('note'), attr_val)

        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('asset_type'), self.__set_asset_type)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('asset_id'), self.__set_asset_id)

        attr_val = self.height_sbox.value()
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('height'), attr_val)

        attr_val = self.network_cbox.itemData(self.network_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('network'), attr_val)

        self.__layer.endEditCommand()

        try:
            PluginUtils.run_query(self.__save_repair_material_and_documents)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        QDialog.accept(self)

    def __save_repair_material_and_documents(self):

        try:
            self.commit()
        except SQLAlchemyError as e:
            raise e

    def __discard_repair_material_and_documents(self):

        self.rollback()

    def reject(self):

        try:
            PluginUtils.run_query(self.__discard_repair_material_and_documents)
        except WntException as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

        QDialog.reject(self)

    def __validate_user_input(self):

        self.received_from_cbox.lineEdit().setText(self.received_from_cbox.lineEdit().text().strip())
        self.repaired_by_cbox.lineEdit().setText(self.repaired_by_cbox.lineEdit().text().strip())
        self.repair_task_cbox.lineEdit().setText(self.repair_task_cbox.lineEdit().text().strip())
        self.note_edit.setPlainText(self.note_edit.toPlainText().strip())

        if self.occurrence_date_chbox.isChecked() and self.occurrence_date_edit.date() > QDate.currentDate():
            PluginUtils.show_message(self, self.tr('Future Date'),
                                     self.tr('The occurrence date must not be in the future!'))
            return False

        if self.registration_date_edit.date() > QDate.currentDate():
            PluginUtils.show_message(self, self.tr('Future Date'),
                                     self.tr('The registration date must not be in the future!'))
            return False

        if self.repair_date_chbox.isChecked() and self.repair_date_edit.date() > QDate.currentDate():
            PluginUtils.show_message(self, self.tr('Future Date'),
                                     self.tr('The repair date must not be in the future!'))
            return False

        if self.repair_date_chbox.isChecked() and len(self.repaired_by_cbox.lineEdit().text()) == 0:
            PluginUtils.show_message(self, self.tr('No Repaired By Entry'),
                                     self.tr('Please enter who fixed the damage!'))
            return False

        if self.__set_asset_type is None or self.__set_asset_id is None:
            PluginUtils.show_message(self, self.tr('No Asset Assigned'),
                                     self.tr('Please assign the asset that was damaged!'))
            return False

        if self.type_cbox.currentIndex() == 0:
            PluginUtils.show_message(self, self.tr('No Damage Type'),
                                     self.tr('Please select the type of damage!'))
            return False

        if self.status_cbox.currentIndex() == 0:
            PluginUtils.show_message(self, self.tr('No Damage Status'),
                                     self.tr('Please provide the status regarding the damage!'))
            return False

        return True

    @pyqtSlot()
    def on_verify_button_clicked(self):

        control_no = self.control_no_sbox.value()

        count = self.session.query(MxWaterLeakageComplaint).filter(MxWaterLeakageComplaint.id == control_no).count()
        if count == 0:
            PluginUtils.show_error(self, self.tr('Verifying Control Number'),
                                     self.tr('Failure: control number not found in MAXCOM database!'))
        else:
            PluginUtils.show_message(self, self.tr('Verifying Control Number'),
                                     self.tr('Success: control number found in MAXCOM database!'))

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            tab_index = self.tabWidget.currentIndex()
            if tab_index == 0:
                PluginUtils.show_help("Add_Edit_Damage.htm")
            elif tab_index == 1:
                PluginUtils.show_help("document_management.html")
            elif tab_index == 2:
                PluginUtils.show_help("Add_Edit_Repair_Material.htm")

    def __populate_nearby_features(self):

        qgs_point = self.__feature.geometry().asPoint()
        x = qgs_point.x()
        y = qgs_point.y()
        sql = "SELECT srid FROM geometry_columns WHERE f_table_name = 'co_fitting'"
        result = self.session.execute(sql).fetchall()
        for row in result:
            srid = row[0]

        self.__nearby_features = []
        self.__find_nearby_features(x, y, srid, 'co_fitting')
        self.__find_nearby_features(x, y, srid, 'co_intake')
        self.__find_nearby_features(x, y, srid, 'co_pipeline_segment')
        self.__find_nearby_features(x, y, srid, 'co_line_casing')
        self.__find_nearby_features(x, y, srid, 'co_bulk_water_meter')
        self.__find_nearby_features(x, y, srid, 'co_meter')
        self.__find_nearby_features(x, y, srid, 'co_distribution_point')
        self.__find_nearby_features(x, y, srid, 'co_connection_point')
        self.__find_nearby_features(x, y, srid, 'co_utility_station')
        self.__find_nearby_features(x, y, srid, 'co_flatrate_connection')
        self.__find_nearby_features(x, y, srid, 'co_manhole')

        self.__populate_damaged_asset_twidget()

    def __find_nearby_features(self, x, y, srid, table_name):

        sql = "SELECT id, ST_Distance(geometry, ST_SetSRID(ST_MakePoint({0}, {1}), {2})) FROM {3} " \
              "WHERE ST_DWithin(geometry, ST_SetSRID(ST_MakePoint({0}, {1}), {2}), 15)".format(x, y, srid, table_name)
        result = self.session.execute(sql).fetchall()
        for row in result:
            id = row[0]
            distance = row[1]
            self.__nearby_features.append((table_name, id, distance))

    def __populate_damaged_asset_twidget(self):

        self.damaged_asset_twidget.clearContents()
        self.damaged_asset_twidget.setRowCount(0)

        count = len(self.__nearby_features)
        self.damaged_asset_twidget.setRowCount(count)

        sorted_assets = sorted(self.__nearby_features, key=lambda asset: asset[2])

        i = 0
        for asset in sorted_assets:

            item = QTableWidgetItem(asset[0])
            self.damaged_asset_twidget.setItem(i, 0, item)

            item = QTableWidgetItem('{}'.format(asset[1]))
            self.damaged_asset_twidget.setItem(i, 1, item)

            item = QTableWidgetItem('{:.2f}'.format(asset[2]))
            self.damaged_asset_twidget.setItem(i, 2, item)

            i += 1

        self.damaged_asset_twidget.resizeColumnsToContents()
        self.damaged_asset_twidget.horizontalHeader().setStretchLastSection(True)

    def __highlight_row(self, asset_type, asset_id):

        # unhighlight all rows first:
        for row in range(self.damaged_asset_twidget.rowCount()):
            self.damaged_asset_twidget.item(row, 0).setBackground(QBrush(Qt.NoBrush))
            self.damaged_asset_twidget.item(row, 1).setBackground(QBrush(Qt.NoBrush))
            self.damaged_asset_twidget.item(row, 2).setBackground(QBrush(Qt.NoBrush))

        found_asset = False

        for row in range(self.damaged_asset_twidget.rowCount()):

            if self.damaged_asset_twidget.item(row, 0).text() == asset_type \
                    and int(self.damaged_asset_twidget.item(row, 1).text()) == asset_id:

                self.damaged_asset_twidget.item(row, 0).setBackground(QtGui.QColor(202, 251, 152))
                self.damaged_asset_twidget.item(row, 1).setBackground(QtGui.QColor(202, 251, 152))
                self.damaged_asset_twidget.item(row, 2).setBackground(QtGui.QColor(202, 251, 152))
                found_asset = True
                break

        if found_asset:
            self.__set_asset_type = asset_type
            self.__set_asset_id = asset_id
            self.warning_label.clear()
        else:
            self.warning_label.setText(self.tr('Reassign asset!'))

        self.damaged_asset_twidget.clearSelection()

    @pyqtSlot()
    def on_set_button_clicked(self):

        if len(self.damaged_asset_twidget.selectionModel().selectedRows()) == 0:
            return

        for index in self.damaged_asset_twidget.selectionModel().selectedRows():
            asset_type = self.damaged_asset_twidget.item(index.row(), 0).text()
            asset_id = int(self.damaged_asset_twidget.item(index.row(), 1).text())
            self.__highlight_row(asset_type, asset_id)

    @pyqtSlot()
    def on_view_maxcom_button_clicked(self):

        control_no = self.control_no_sbox.value()

        if control_no > -1:
            PluginUtils.open_maxcom(control_no, 'COMPLAINT_DAMAGE')
