from __future__ import print_function
from __future__ import absolute_import
from builtins import object
from .controller.EditAssetTool import *
from .controller.PipelineSegmentDialog import *
from .controller.FittingDialog import *
from .controller.ManholeDialog import *
from .controller.IntakeDialog import *
from .controller.FlatrateConnectionDialog import *
from .controller.MeterDialog import *
from .controller.DamageDialog import *
from .controller.DistributionPointDialog import *
from .controller.UtilityStationDialog import *
from .controller.LineCasingDialog import *
from .controller.ConnectionPointDialog import *
from .controller.BulkWaterMeterDialog import *
from .controller.UserSettingsDialog import *
from .controller.NetworkManagementDialog import *
from .utils.SessionHandler import *
from .view.resources_rc import *
import os
from distutils import spawn
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *


class WntOS(object):

    def __init__(self, iface):

        self.iface = iface
        self.map_canvas = iface.mapCanvas()
        self.map_layer_registry = QgsProject.instance()
        self.map_layer_registry.layerWasAdded.connect(self.__layer_added)

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        override_locale = QSettings().value("locale/overrideFlag", False, type=bool)
        if not override_locale:
            locale = QLocale.system().name()
        else:
            locale = QSettings().value("locale/userLocale", "", type=str)

        self.translator = QTranslator()
        if self.translator.load("WntOS_" + locale, self.plugin_dir):
            QApplication.installTranslator(self.translator)

        self.actions = []
        self.toolbar = self.iface.addToolBar(self.tr("WNT Open Source 3"))
        self.menu = QMenu(self.tr("WNT Open Source 3"))
        self.help_action = None
        self.edit_asset_action = None
        self.settings_action = None
        self.build_topology_action = None
        self.reverse_flow_action = None
        self.network_management_action = None
        self.__feat_id = None
        self.map_tool = EditAssetTool(self)

        self.__add_repository()

    def tr(self, message):

        return QApplication.translate('Plugin', message)

    def add_action(self, icon_path, text, callback, menu, add_to_menu=True, add_to_toolbar=True,
                   status_tip=None, whats_this=None, parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            menu.addAction(action)

        self.actions.append(action)

        return action

    def __add_repository(self):

        QSettings().setValue(Constants.CHECK_FOR_PLUGIN_UPDATES_PARAM, True)
        QSettings().setValue(Constants.CHECK_FOR_PLUGIN_UPDATES_INTERVAL_PARAM, 1)
        QSettings().setValue(Constants.ALLOWED_PLUGIN_TYPE_PARAM, 2)
        repository = QSettings().value(Constants.REPOSITORY_URL_PARAM, -999)
        if repository == -999:
            QSettings().setValue(Constants.REPOSITORY_URL_PARAM, Constants.REPOSITORY_URL)
            QSettings().setValue(Constants.REPOSITORY_ENABLED_PARAM, True)

    def __destroy_db_session(self):

        SessionHandler().destroy_session()

    def initGui(self):

        menu_bar = self.iface.mainWindow().menuBar()
        menu_bar.addMenu(self.menu)

        self.edit_asset_action = self.add_action(
            ":/wnt/edit.png",
            text=self.tr("View/Edit Asset Details"),
            callback=self.__edit_asset,
            menu=self.menu,
            parent=self.iface.mainWindow())

        self.edit_asset_action.setCheckable(True)

        self.network_management_action = self.add_action(
            ":/wnt/network.png",
            text=self.tr("Manage Networks"),
            callback=self.__manage_networks,
            menu=self.menu,
            parent=self.iface.mainWindow())

        self.menu.addSeparator()
        self.toolbar.addSeparator()

        self.build_topology_action = self.add_action(
            ":/wnt/build_topology.png",
            text=self.tr("Build/Update Topology"),
            callback=self.__build_topology,
            menu=self.menu,
            parent=self.iface.mainWindow())

        self.reverse_flow_action = self.add_action(
            ":/wnt/reverse_flow.png",
            text=self.tr("Reverse Flow Direction"),
            callback=self.__reverse_flow,
            menu=self.menu,
            parent=self.iface.mainWindow())

        self.menu.addSeparator()
        self.toolbar.addSeparator()

        self.settings_action = self.add_action(
            ":/wnt/settings.png",
            text=self.tr("User Settings"),
            callback=self.__show_settings_dialog,
            menu=self.menu,
            parent=self.iface.mainWindow())

        self.menu.addSeparator()

        self.help_action = self.add_action(
            ":/wnt/help.png",
            text=self.tr("Help"),
            callback=self.__show_help,
            menu=self.menu,
            parent=self.iface.mainWindow())

        self.__disable_tool_access()

    def unload(self):

        for action in self.actions:
            self.menu.removeAction(action)

        self.iface.mainWindow().removeToolBar(self.toolbar)
        del self.toolbar
        del self.menu
        self.map_tool.set_plugin_unloaded()
        self.__destroy_db_session()

    def __layer_added(self, layer):

        if layer.type() == QgsMapLayer.VectorLayer and layer.dataProvider().name() == "postgres":
            uri_string = layer.dataProvider().dataSourceUri()
            uri = QgsDataSourceUri(uri_string)
            if uri.schema() == 'core' and uri.table()[:3] == 'co_':
                layer.featureAdded.connect(self.__feature_added)
                # Required because of the current limitations regarding QGIS
                # edit buffer:
                layer.undoStack().indexChanged.connect(self.__undo_stack_changed)
                edit_form_config = layer.editFormConfig()
                edit_form_config.setSuppress(1)

                if SessionHandler().session_instance() is None:
                    user = uri.username()
                    password = uri.password()
                    hostname = uri.host()
                    port = uri.port()
                    database = uri.database()
                    try:
                        SessionHandler().create_session(user, password, hostname, port, database)
                        self.__set_tool_access()
                    except WntException as e:
                        PluginUtils.show_error(None, e.args[1], e.args[0])

    def __fitting_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Fitting added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = FittingDialog(layer, feature_id)
            dlg.exec_()

    def __pipeline_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Pipeline added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = PipelineSegmentDialog(layer, feature_id)
            dlg.exec_()

    def __utility_station_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Utility station added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = UtilityStationDialog(layer, feature_id)
            dlg.exec_()

    def __manhole_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Manhole added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = ManholeDialog(layer, feature_id)
            dlg.exec_()

    def __dma_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('DMA added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = DMADialog(layer, feature_id)
            dlg.exec_()

    def __feature_added(self, feature_id):

        self.__feat_id = feature_id

    def __undo_stack_changed(self, cmd_id):

        layer = self.iface.legendInterface().currentLayer()
        command = layer.undoStack().command(cmd_id)
        if command and 'co_' in command.actionText():
            return
        command = layer.undoStack().command(cmd_id - 1)
        if command and command.actionText() == 'add feature':

            uri_string = layer.dataProvider().dataSourceUri()
            uri = QgsDataSourceUri(uri_string)
            if uri.table() == 'co_fitting':
                self.__fitting_added(self.__feat_id)
            elif uri.table() == 'co_pipeline_segment':
                self.__pipeline_added(self.__feat_id)
            elif uri.table() == 'co_utility_station':
                self.__utility_station_added(self.__feat_id)
            elif uri.table() == 'co_manhole':
                self.__manhole_added(self.__feat_id)
            elif uri.table() == 'co_dma':
                self.__dma_added(self.__feat_id)
            elif uri.table() == 'co_flatrate_connection':
                self.__flatrate_connection_added(self.__feat_id)
            elif uri.table() == 'co_intake':
                self.__intake_added(self.__feat_id)
            elif uri.table() == 'co_line_casing':
                self.__line_casing_added(self.__feat_id)
            elif uri.table() == 'co_connection_point':
                self.__connection_point_added(self.__feat_id)
            elif uri.table() == 'co_meter':
                self.__meter_added(self.__feat_id)
            elif uri.table() == 'co_distribution_point':
                self.__distribution_point_added(self.__feat_id)
            elif uri.table() == 'co_bulk_water_meter':
                self.__bulk_water_meter_added(self.__feat_id)
            elif uri.table() == 'co_damage':
                self.__damage_added(self.__feat_id)

    def __flatrate_connection_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Flatrate connection added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = FlatrateConnectionDialog(layer, feature_id)
            dlg.exec_()

    def __intake_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Intake added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = IntakeDialog(layer, feature_id)
            dlg.exec_()

    def __line_casing_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Line casing added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = LineCasingDialog(layer, feature_id)
            dlg.exec_()

    def __connection_point_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Connection point added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = ConnectionPointDialog(layer, feature_id)
            dlg.exec_()

    def __meter_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Meter added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = MeterDialog(layer, feature_id)
            dlg.exec_()

    def __distribution_point_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Distribution point added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = DistributionPointDialog(layer, feature_id)
            dlg.exec_()

    def __bulk_water_meter_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Bulk water meter added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = BulkWaterMeterDialog(layer, feature_id)
            dlg.exec_()

    def __damage_added(self, feature_id):

        layer = self.iface.legendInterface().currentLayer()
        # fix_print_with_import
        print('Damage added: {0}'.format(feature_id))
        if feature_id < 0:
            dlg = DamageDialog(layer, feature_id)
            dlg.exec_()

    def __show_help(self):

        # detect OS to show help file correctly
        if sys.platform == "linux" or sys.platform == "linux2":

            xchmPath = spawn.find_executable("xchm")

            if xchmPath is None:
                help_path = os.path.abspath(os.path.join(
                    os.path.dirname(__file__), "manual/wnt_help.chm"))
                QMessageBox.information(None, self.tr("Help File on Linux"), self.tr(
                    "Please install 'xchm' to view HTML help file.\n\nFor example:\nsudo apt-get install xchm\n\nOr, open the file with any other CHM compatible program. The file can be found at: {}").format(help_path))
            else:
                PluginUtils.show_help("introduction.html")

        elif sys.platform == "win32":
            PluginUtils.show_help("introduction.html")

    def __disable_tool_access(self):

        for action in self.actions:

            if action != self.help_action:
                action.setEnabled(False)

    def __set_tool_access(self):

        user_groups = SessionHandler().user_rights()
        for group in user_groups:

            if group == 'uwasa_codelist':
                pass
            elif group == 'uwasa_update' or group == 'uwasa_view':
                self.edit_asset_action.setEnabled(True)
                self.settings_action.setEnabled(True)
                self.network_management_action.setEnabled(True)
            if group == 'uwasa_update':
                self.build_topology_action.setEnabled(True)
                self.reverse_flow_action.setEnabled(True)

    def __edit_asset(self):

        self.map_tool.setAction(self.edit_asset_action)
        self.map_canvas.setMapTool(self.map_tool)

    def __show_settings_dialog(self):

        dlg = UserSettingsDialog()
        dlg.exec_()

    def __manage_networks(self):

        dlg = NetworkManagementDialog()
        dlg.exec_()

    def __build_topology(self):

        if QMessageBox.No == QMessageBox.question(None, self.tr('Build/Update Topology'),
                                                  self.tr(
                                                      'Build/update topology?'),
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No):
            return

        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        try:
            PluginUtils.build_topology()
            QApplication.restoreOverrideCursor()
            PluginUtils.show_message(None, self.tr('Build/Update Topology'),
                                     self.tr('Topology built/updated successfully.'))
        except SQLAlchemyError as e:
            QApplication.restoreOverrideCursor()
            PluginUtils.show_error(None, self.tr(
                'Build/Update Topology'), e.args[0])

    def __reverse_flow(self):

        pipeline_layer = LayerUtils.layer_by_data_source(
            'core', 'co_pipeline_segment')
        if pipeline_layer is None:
            return

        feat_ids = pipeline_layer.selectedFeatureIds()
        if len(feat_ids) == 0:
            PluginUtils.show_message(None, self.tr('Reverse Flow Direction'),
                                     self.tr('No pipeline(s) selected!'))
            return

        if QMessageBox.No == QMessageBox.question(None, self.tr('Reverse Flow Direction'),
                                                  self.tr('Reverse flow direction for {} pipeline(s)?'.format(
                                                      len(feat_ids))),
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No):
            return

        try:
            PluginUtils.reverse_flow_direction(feat_ids, self.map_canvas)
            PluginUtils.show_message(None, self.tr('Reverse Flow Direction'),
                                     self.tr('Flow direction reversed for selected pipeline(s).'))
        except SQLAlchemyError as e:
            PluginUtils.show_error(None, self.tr(
                'Reverse Flow Direction'), e.args[0])

        pass
