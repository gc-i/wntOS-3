from __future__ import print_function
from __future__ import absolute_import
from builtins import range
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_FindFeatureDialog import *
from .FittingDialog import *
from .PipelineSegmentDialog import *
from .ManholeDialog import *
from .IntakeDialog import *
from .FlatrateConnectionDialog import *
from .MeterDialog import *
from .DistributionPointDialog import *
from .UtilityStationDialog import *
from .LineCasingDialog import *
from .ConnectionPointDialog import *
from .BulkWaterMeterDialog import *
from .DMADialog import *
from .DamageDialog import *
from ..utils.LayerUtils import *


class FindFeatureDialog(QDialog, Ui_FindFeatureDialog):

    selection_changed = pyqtSignal(int)

    def __init__(self, parent=None):

        super(FindFeatureDialog, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.__layer = None

    def set_features(self, feature_list, layer):

        self.list_title_label.setText(self.tr('Features ({0}):'.format(layer.name())))

        self.__layer = layer
        self.feature_lwidget.clear()
        for feat_id in feature_list:
            item = QListWidgetItem('Feature {0}'.format(feat_id))
            item.setData(Qt.UserRole, feat_id)
            self.feature_lwidget.addItem(item)

        if len(feature_list) > 0:
            self.feature_lwidget.setCurrentRow(0)

    @pyqtSlot(int)
    def on_feature_lwidget_currentRowChanged(self, row):

        if row == -1:
            return
        # fix_print_with_import
        print("Row: {}".format(row))
        feat_id = self.feature_lwidget.item(row).data(Qt.UserRole)
        self.selection_changed.emit(feat_id)

    @pyqtSlot("QListWidgetItem*")
    def on_feature_lwidget_itemDoubleClicked(self, item):

        feat_id = item.data(Qt.UserRole)
        table_name = LayerUtils.table_name_by_layer(self.__layer)

        if table_name == 'co_fitting':
            dlg = FittingDialog(self.__layer, feat_id, True)
        elif table_name == 'co_pipeline_segment':
            dlg = PipelineSegmentDialog(self.__layer, feat_id, True)
        elif table_name == 'co_utility_station':
            dlg = UtilityStationDialog(self.__layer, feat_id, True)
        elif table_name == 'co_manhole':
            dlg = ManholeDialog(self.__layer, feat_id, True)
        elif table_name == 'co_dma':
            dlg = DMADialog(self.__layer, feat_id, True)
        elif table_name == 'co_flatrate_connection':
            dlg = FlatrateConnectionDialog(self.__layer, feat_id, True)
        elif table_name == 'co_intake':
            dlg = IntakeDialog(self.__layer, feat_id, True)
        elif table_name == 'co_line_casing':
            dlg = LineCasingDialog(self.__layer, feat_id, True)
        elif table_name == 'co_connection_point':
            dlg = ConnectionPointDialog(self.__layer, feat_id, True)
        elif table_name == 'co_meter':
            dlg = MeterDialog(self.__layer, feat_id, True)
        elif table_name == 'co_distribution_point':
            dlg = DistributionPointDialog(self.__layer, feat_id, True)
        elif table_name == 'co_bulk_water_meter':
            dlg = BulkWaterMeterDialog(self.__layer, feat_id, True)
        elif table_name == 'co_damage':
            dlg = DamageDialog(self.__layer, feat_id, True)

        dlg.exec_()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("introduction.html")

    def feature_added(self, layer_id, added_features):

        table_name = LayerUtils.table_name_by_layer(self.__layer)

        if table_name in layer_id:
            for row in range(self.feature_lwidget.count()):
                feat_id = self.feature_lwidget.item(row).data(Qt.UserRole)
                if feat_id < 0:
                    self.feature_lwidget.clear()
                    break
