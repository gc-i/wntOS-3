from __future__ import print_function
from __future__ import absolute_import
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_DMADialog import *
from .DocumentForm import *
from ..utils.PluginUtils import PluginUtils
from sqlalchemy.exc import SQLAlchemyError
from ..model.DatabaseHelper import *
from qgis.core import QgsFeatureRequest


class DMADialog(QDialog, Ui_DMADialog, DatabaseHelper):

    def __init__(self, layer, feature_id, attr_update=False, parent=None):

        super(DMADialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__layer = layer
        self.__feature_id = feature_id
        self.__attr_update = attr_update
        self.__feature = None

        if not layer.isEditable():
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        try:
            PluginUtils.run_query(PluginUtils.populate_network_cbox, 2, self.network_cbox)
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

        self.document_form = DocumentForm('co_dma', self.__feature_id)
        self.tabWidget.addTab(self.document_form, 'Documents')

        if attr_update:
            self.__populate_details()

    def feature_id(self):

        return self.__feature_id

    def __populate_details(self):

        feature = self.__feature

        if feature['dma_number']:
            self.dma_number_edit.setText(feature['dma_number'])
        if feature['dma_name']:
            self.dma_name_edit.setText(feature['dma_name'])
        if feature['area']:
            self.area_edit.setText('{:.2f}'.format(feature['area']/1000000))
        if feature['network']:
            self.network_cbox.setCurrentIndex(self.network_cbox.findData(feature['network'], Qt.UserRole))

    def accept(self):

        if not self.__validate_user_input():
            return

        feature = self.__feature

        self.__layer.beginEditCommand('Update attributes (co_dma)')

        attr_val = self.dma_number_edit.text() if len(self.dma_number_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('dma_number'), attr_val)

        attr_val = self.dma_name_edit.text() if len(self.dma_name_edit.text()) > 0 else None
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('dma_name'), attr_val)

        attr_val = self.network_cbox.itemData(self.network_cbox.currentIndex(), Qt.UserRole)
        self.__layer.changeAttributeValue(self.__feature_id, feature.fieldNameIndex('network'), attr_val)

        self.__layer.endEditCommand()

        try:
            PluginUtils.run_query(self.__save_documents)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        QDialog.accept(self)

    def __save_documents(self):

        try:
            self.commit()
        except SQLAlchemyError as e:
            raise e

    def __discard_documents(self):

        self.rollback()

    def reject(self):

        try:
            PluginUtils.run_query(self.__discard_documents)
        except WntException as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

        QDialog.reject(self)

    def __validate_user_input(self):

        self.dma_number_edit.setText(self.dma_number_edit.text().strip())
        return True

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            tab_index = self.tabWidget.currentIndex()
            if tab_index == 0:
                PluginUtils.show_help("Add_Edit_DMA.htm")
            elif tab_index == 1:
                PluginUtils.show_help("document_management.html")



