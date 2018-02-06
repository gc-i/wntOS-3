from __future__ import absolute_import
from qgis.gui import QgsMapTool, QgsRubberBand, QgsMapLayerComboBox
from qgis.core import *
from ..utils.LayerUtils import *
from .FindFeatureDialog import *


class EditAssetTool(QgsMapTool):

    def __init__(self, plugin):

        QgsMapTool.__init__(self, plugin.map_canvas)

        self.plugin = plugin
        self.doubleclick = False
        self.__plugin_unloaded = False

        self.current_dialog = None
        self.dialog_position = None
        self.feature_list = dict()
        self.layer = None
        self.connected_layers = None

        settings = QSettings()
        qgsLineWidth = 2  # use fixed width
        qgsLineRed = settings.value("/qgis/digitizing/line_color_red", 255, type=int)
        qgsLineGreen = settings.value("/qgis/digitizing/line_color_green", 0, type=int)
        qgsLineBlue = settings.value("/qgis/digitizing/line_color_blue", 0, type=int)

        self.rubBandPol = QgsRubberBand(plugin.map_canvas)
        self.rubBandPol.setColor(QColor(qgsLineRed, qgsLineGreen, qgsLineBlue))
        self.rubBandPol.setWidth(qgsLineWidth)
    
    def activate(self):

        super(EditAssetTool, self).activate()
        self.plugin.iface.mainWindow().statusBar().showMessage(self.tr("Click on an asset!"))
        self.connected_layers = list()

    def canvasDoubleClickEvent(self, event):

        self.doubleclick = True
               
    def canvasReleaseEvent(self, event):

        if self.doubleclick:
            self.doubleclick = False
            return

        if event.button() != Qt.LeftButton:
            return

        self.layer = QgsMapLayerComboBox().currentLayer()
        if self.layer is None:
            return

        # find out map coordinates from mouse click
        map_point = self.toLayerCoordinates(self.layer, event.pos())
        tolerance = self.searchRadiusMU(self.plugin.map_canvas)
        area = QgsRectangle(map_point.x() - tolerance, map_point.y() - tolerance,
                            map_point.x() + tolerance, map_point.y() + tolerance)

        request = QgsFeatureRequest()
        request.setFilterRect(area).setFlags(QgsFeatureRequest.ExactIntersect)
        request.setSubsetOfAttributes([0])

        result = False

        feature_id_list = list()
        self.feature_list.clear()

        for feature in self.layer.getFeatures(request):

            self.feature_list[feature.id()] = feature
            feature_id_list.append(feature.id())
            result = True

        if not result:
            if self.current_dialog:
                self.current_dialog.hide()
                self.dialog_position = self.current_dialog.pos()
                self.rubBandPol.reset(True)
        else:
            if not self.current_dialog:
                self.current_dialog = FindFeatureDialog(self.plugin.iface.mainWindow())
                self.current_dialog.rejected.connect(self.__clean_up)
                self.current_dialog.selection_changed.connect(self.__hightlight_feature)

            if self.dialog_position and self.current_dialog.isHidden():
                self.current_dialog.move(self.dialog_position)

            if self.current_dialog.isHidden():
                self.current_dialog.show()

            self.current_dialog.set_features(feature_id_list, self.layer)

        if self.layer not in self.connected_layers and self.current_dialog:
            self.layer.committedFeaturesAdded.connect(self.current_dialog.feature_added)
            self.connected_layers.append(self.layer)

    @pyqtSlot(int)
    def __hightlight_feature(self, feature_id):

        feature = self.feature_list[feature_id]

        if feature.geometry().type() == QgsWkbTypes.Point:
            self.rubBandPol.reset(QgsWkbTypes.PointGeometry)
        elif feature.geometry().type() == QgsWkbTypes.Line:
            self.rubBandPol.reset(QgsWkbTypes.LineGeometry)
        else:
            self.rubBandPol.reset(QgsWkbTypes.PolygonGeometry)

        self.rubBandPol.addGeometry(feature.geometry(), self.layer)

    def deactivate(self):

        if self.__plugin_unloaded:
            return

        self.plugin.iface.mainWindow().statusBar().showMessage("")
        self.doubleclick = False
        self.rubBandPol.reset()
        if self.current_dialog:
            self.current_dialog.reject()

        super(EditAssetTool, self).deactivate()

    def set_plugin_unloaded(self):

        self.__plugin_unloaded = True

    def __clean_up(self):

        self.current_dialog = None
        self.dialog_position = None
        self.rubBandPol.reset()
