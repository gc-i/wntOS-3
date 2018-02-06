from __future__ import absolute_import
from PyQt5.QtWidgets import *
from ..view.Ui_NetworkDialog import *
from ..model.core_classes import CoNetwork, ClNominalPressure
from .DocumentForm import *


class NetworkDialog(QDialog, Ui_NetworkDialog, DatabaseHelper):

    def __init__(self, network_id, parent=None):

        super(NetworkDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__network_id = network_id

        try:
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.dim_pressure_cbox,
                                  ClNominalPressure, True)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.op_pressure_cbox,
                                  ClNominalPressure, True)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            return

        if network_id is None:
            co_network = CoNetwork()
            co_network.network_number = 'XXX'
            co_network.network_name = 'XXX'
            self.session.add(co_network)
            self.session.flush()
            self.__network_id = co_network.id
        else:
            self.__populate_network_details()

        self.document_form = DocumentForm('co_network', self.__network_id)
        self.tabWidget.addTab(self.document_form, 'Documents')

    def network_id(self):

        return self.__network_id

    def __populate_network_details(self):

        co_network = self.session.query(CoNetwork).get(self.__network_id)

        self.network_no_edit.setText(co_network.network_number)

        self.network_name_edit.setText(co_network.network_name)

        if co_network.dimensioning_pressure is not None:
            self.dim_pressure_cbox.setCurrentIndex(self.dim_pressure_cbox.
                                                   findData(co_network.dimensioning_pressure, Qt.UserRole))

        if co_network.operating_pressure is not None:
            self.op_pressure_cbox.setCurrentIndex(self.op_pressure_cbox.
                                                  findData(co_network.operating_pressure, Qt.UserRole))

    def accept(self):

        if not self.__validate_user_input():
            return

        network_number = self.network_no_edit.text()
        network_name = self.network_name_edit.text()
        dim_pressure = self.dim_pressure_cbox.itemData(self.dim_pressure_cbox.currentIndex(), Qt.UserRole)
        op_pressure = self.op_pressure_cbox.itemData(self.op_pressure_cbox.currentIndex(), Qt.UserRole)

        self.create_savepoint()
        try:
            co_network = self.session.query(CoNetwork).get(self.__network_id)
            co_network.network_number = network_number
            co_network.network_name = network_name
            co_network.dimensioning_pressure = dim_pressure
            co_network.operating_pressure = op_pressure
            self.session.add(co_network)

            self.commit()

        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            if 'network_number' in e.args[0] and 'duplicate key' in e.args[0]:
                PluginUtils.show_error(self, self.tr('Duplicate Network Number'),
                                       self.tr('A network with the same number already exists.'))
            elif 'network_name' in e.args[0] and 'duplicate key' in e.args[0]:
                PluginUtils.show_error(self, self.tr('Duplicate Network Name'),
                                       self.tr('A network with the same name already exists.'))
            else:
                PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        QDialog.accept(self)

    def reject(self):

        self.rollback()

        QDialog.reject(self)

    def __validate_user_input(self):

        self.network_no_edit.setText(self.network_no_edit.text().strip())
        self.network_name_edit.setText(self.network_name_edit.text().strip())

        if len(self.network_no_edit.text()) == 0:
            PluginUtils.show_message(self, self.tr('No Network Number'), self.tr('Please provide a network number!'))
            return False

        if len(self.network_name_edit.text()) == 0:
            PluginUtils.show_message(self, self.tr('No Network Name'), self.tr('Please provide a network name!'))
            return False

        return True

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("manage_networks.html")
