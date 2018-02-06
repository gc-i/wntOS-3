from __future__ import absolute_import
from builtins import str
from builtins import object
from qgis.core import *
from .SessionHandler import SessionHandler


class LayerUtils(object):

    @staticmethod
    def layer_by_name(layer_name):
        layers = QgsProject.instance().mapLayers()

        for id, layer in layers.items():
            if layer.name() == layer_name:
                return layer

        return None

    @staticmethod
    def layer_by_data_source(schema_name, table_name):

        layers = QgsProject.instance().mapLayers()

        for id, layer in layers.items():
            if layer.type() == QgsMapLayer.VectorLayer:
                uri_string = layer.dataProvider().dataSourceUri()
                uri = QgsDataSourceUri(uri_string)
                if uri.table() == table_name:
                    if uri.schema() == schema_name:
                        return layer

        return None

    @staticmethod
    def load_database_layer(schema_name, table_name):

        uri = QgsDataSourceUri()
        user = SessionHandler().current_username()
        db = SessionHandler().current_database()
        host = SessionHandler().current_host()
        port = SessionHandler().current_port()
        pwd = SessionHandler().current_password()

        uri.setConnection(host, str(port), db, user, pwd)
        uri.setDataSource(schema_name, table_name, "geometry")
        vlayer = QgsVectorLayer(uri.uri(), table_name, "postgres")
        QgsProject.instance().addMapLayer(vlayer)
        return vlayer

    @staticmethod
    def deselect_all():

        layers = QgsProject.instance().mapLayers()

        for id, layer in layers.items():
            if layer.type() == QgsMapLayer.VectorLayer:
                layer.removeSelection()

    @staticmethod
    def clear_selection(schema, table_name):

        layer = LayerUtils.layer_by_data_source(schema, table_name)
        if layer is not None:
            layer.removeSelection()

    @staticmethod
    def table_name_by_layer(layer):

        if layer.type() == QgsMapLayer.VectorLayer and layer.dataProvider().name() == "postgres":
            uri_string = layer.dataProvider().dataSourceUri()
            uri = QgsDataSourceUri(uri_string)
            return uri.table()

        return None
