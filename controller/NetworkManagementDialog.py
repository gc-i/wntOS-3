from __future__ import absolute_import
from PyQt5.QtWidgets import *
from builtins import range
from ..view.Ui_NetworkManagementDialog import *
from ..model.core_classes import CoNetwork
from ..utils.PluginUtils import *
from .NetworkDialog import *


class NetworkManagementDialog(QDialog, Ui_NetworkManagementDialog, DatabaseHelper):

    def __init__(self, parent=None):

        super(NetworkManagementDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        try:
            PluginUtils.run_query(self.__populate_network_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.add_network_button.setEnabled(False)
            self.edit_network_button.setEnabled(False)
            self.delete_network_button.setEnabled(False)

    def __populate_network_twidget(self):

        self.network_twidget.clearContents()
        self.network_twidget.setRowCount(0)

        count = self.session.query(CoNetwork).count()
        self.network_twidget.setRowCount(count)

        i = 0
        for co_network in self.session.query(CoNetwork).order_by(CoNetwork.network_number):

            item = QTableWidgetItem(co_network.network_number)
            item.setData(Qt.UserRole, co_network.id)
            self.network_twidget.setItem(i, 0, item)

            item = QTableWidgetItem(co_network.network_name)
            self.network_twidget.setItem(i, 1, item)

            if co_network.cl_dimensioning_pressure is not None:
                description = co_network.cl_dimensioning_pressure.description
                item = QTableWidgetItem(description)
                self.network_twidget.setItem(i, 2, item)

            if co_network.cl_operating_pressure is not None:
                description = co_network.cl_operating_pressure.description
                item = QTableWidgetItem(description)
                self.network_twidget.setItem(i, 3, item)

            i += 1

        self.network_twidget.resizeColumnsToContents()
        self.network_twidget.horizontalHeader().setStretchLastSection(True)

    @pyqtSlot()
    def on_add_network_button_clicked(self):

        dlg = NetworkDialog(None, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__reload_and_select_network(dlg.network_id())

    @pyqtSlot()
    def on_edit_network_button_clicked(self):

        if len(self.network_twidget.selectionModel().selectedRows()) == 0:
            return

        for index in self.network_twidget.selectionModel().selectedRows():
            network_id = self.network_twidget.item(index.row(), 0).data(Qt.UserRole)

        dlg = NetworkDialog(network_id, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__reload_and_select_network(network_id)

    @pyqtSlot()
    def on_delete_network_button_clicked(self):

        if len(self.network_twidget.selectionModel().selectedRows()) == 0:
            return

        if QMessageBox.No == QMessageBox.question(self, self.tr("Delete Network"),
                                                  self.tr('All references to that network will be set to NULL. Delete the selected network?'),
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No):
            return

        for index in self.network_twidget.selectionModel().selectedRows():
            row = index.row()
            network_id = self.network_twidget.item(row, 0).data(Qt.UserRole)

        try:
            PluginUtils.run_query(self.__delete_network, 2, network_id)
            self.network_twidget.removeRow(row)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

    def __delete_network(self, network_id):

        co_network = self.session.query(CoNetwork).get(network_id)
        self.create_savepoint()
        try:
            self.session.delete(co_network)
            self.commit()
        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

    def __reload_and_select_network(self, network_id):

        try:
            PluginUtils.run_query(self.__populate_network_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        self.__select_network(network_id)
        self.network_twidget.setFocus()

    def __select_network(self, network_id):

        for row in range(self.network_twidget.rowCount()):
            network_id_2 = self.network_twidget.item(row, 0).data(Qt.UserRole)
            if network_id_2 == network_id:
                self.network_twidget.selectRow(row)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("manage_networks.html")
