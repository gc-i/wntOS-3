from builtins import range
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ..view.Ui_CustomerManagementForm import *
from ..model.DatabaseHelper import *
from ..model.core_classes import MxCustomer, CoDistributionPointCustomer, CoDistributionPoint, MxTariffCategory
from ..utils.PluginUtils import *
from sqlalchemy import and_, or_


class CustomerManagementForm(QWidget, Ui_CustomerManagementForm, DatabaseHelper):

    def __init__(self, asset_class, asset_id, parent=None):

        super(CustomerManagementForm, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__asset_class = asset_class
        self.__asset_id = asset_id
        try:
            PluginUtils.run_query(self.__populate_assigned_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.assign_cust_button.setEnabled(False)
            self.unassign_cust_button.setEnabled(False)

        self.search_term_edit.setFocus()

    def __populate_assigned_twidget(self):

        self.assigned_cust_twidget.clearContents()
        self.assigned_cust_twidget.setRowCount(0)

        if self.__asset_class != CoDistributionPoint:
            count = self.session.query(MxCustomer).join(self.__asset_class,
                                                        MxCustomer.id == self.__asset_class.maxcom_customer). \
                                                        filter(self.__asset_class.id == self.__asset_id).count()
        else:
            count = self.session.query(MxCustomer).\
                join(CoDistributionPointCustomer, MxCustomer.id == CoDistributionPointCustomer.maxcom_customer). \
                filter(CoDistributionPointCustomer.distribution_point == self.__asset_id).count()
        
        self.assigned_cust_twidget.setRowCount(count)

        i = 0

        if self.__asset_class != CoDistributionPoint:
            for customer in self.session.query(MxCustomer).join(self.__asset_class,
                                                        MxCustomer.id == self.__asset_class.maxcom_customer). \
                                                        filter(self.__asset_class.id == self.__asset_id).\
                                                        order_by(MxCustomer.cons_name):
                self.__add_row(customer, i, self.assigned_cust_twidget)
                i += 1

        else:
            for customer in self.session.query(MxCustomer). \
                    join(CoDistributionPointCustomer, MxCustomer.id == CoDistributionPointCustomer.maxcom_customer).\
                    filter(CoDistributionPointCustomer.distribution_point == self.__asset_id). \
                    order_by(MxCustomer.cons_name):

                self.__add_row(customer, i, self.assigned_cust_twidget)
                i += 1

        self.assigned_cust_twidget.resizeColumnsToContents()
        self.assigned_cust_twidget.horizontalHeader().setStretchLastSection(True)

    def __add_row(self, customer, i, twidget):

        item = QTableWidgetItem(customer.id_number)
        item.setData(Qt.UserRole, customer.id)
        twidget.setItem(i, 0, item)

        item = QTableWidgetItem(customer.cons_name)
        twidget.setItem(i, 1, item)

        item = QTableWidgetItem(customer.address)
        twidget.setItem(i, 2, item)

        item = QTableWidgetItem(customer.house_no)
        twidget.setItem(i, 3, item)

        item = QTableWidgetItem(customer.city)
        twidget.setItem(i, 4, item)

        item = QTableWidgetItem(customer.can)
        twidget.setItem(i, 5, item)

        item = QTableWidgetItem(customer.status)
        twidget.setItem(i, 6, item)

        if customer.tariff_category_master_id is not None:
            mx_tariff_category = self.session.query(MxTariffCategory).\
                filter(MxTariffCategory.id == customer.tariff_category_master_id).one()
            item = QTableWidgetItem(mx_tariff_category.tariff_category)
            twidget.setItem(i, 7, item)

    @pyqtSlot()
    def on_assign_cust_button_clicked(self):

        if self.__asset_id < 0:
            PluginUtils.show_message(self, self.tr("Asset not saved yet"),
                                     self.tr("You must save your changes to database before assigning a customer."))
            return

        if len(self.registered_cust_twidget.selectionModel().selectedRows()) == 0:
            return

        if len(self.assigned_cust_twidget.selectionModel().selectedRows()) > 0 \
                and self.__asset_class != CoDistributionPoint:

            PluginUtils.show_message(self, self.tr("Too many customers"),
                                     self.tr("Only one customer can be assigned."))
            return

        for index in self.registered_cust_twidget.selectionModel().selectedRows():
            customer_id = self.registered_cust_twidget.item(index.row(), 0).data(Qt.UserRole)

        if self.__asset_class == CoDistributionPoint and self.__customer_assigned(customer_id):
                return

        try:
            PluginUtils.run_query(self.__assign_customer, 2, customer_id)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

    def __assign_customer(self, customer_id):

        if self.__asset_class != CoDistributionPoint:
            asset = self.session.query(self.__asset_class).get(self.__asset_id)
            asset.maxcom_customer = customer_id
        else:
            co_distpoint_customer = CoDistributionPointCustomer()
            co_distpoint_customer.distribution_point = self.__asset_id
            co_distpoint_customer.maxcom_customer = customer_id
            self.session.add(co_distpoint_customer)

        self.__populate_assigned_twidget()

    @pyqtSlot()
    def on_unassign_cust_button_clicked(self):

        if len(self.assigned_cust_twidget.selectionModel().selectedRows()) == 0:
            return

        if QMessageBox.No == QMessageBox.question(self, self.tr("Unassign Customer"),
                                                  self.tr('Unassign the selected customer?'),
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No):
            return

        try:
            PluginUtils.run_query(self.__unassign_customer)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

    def __unassign_customer(self):

        self.create_savepoint()
        try:
            if self.__asset_class != CoDistributionPoint:
                asset = self.session.query(self.__asset_class).get(self.__asset_id)
                asset.maxcom_customer = None
            else:
                for index in self.assigned_cust_twidget.selectionModel().selectedRows():
                    customer_id = self.assigned_cust_twidget.item(index.row(), 0).data(Qt.UserRole)
                co_distpoint_customer = self.session.query(CoDistributionPointCustomer).\
                    filter(and_(CoDistributionPointCustomer.distribution_point == self.__asset_id,
                           CoDistributionPointCustomer.maxcom_customer == customer_id)).one()
                self.session.delete(co_distpoint_customer)

            self.__populate_assigned_twidget()
            self.release_savepoint()

        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

    def __customer_assigned(self, customer_id):

        for row in range(self.assigned_cust_twidget.rowCount()):
            customer_id2 = self.assigned_cust_twidget.item(row, 0).data(Qt.UserRole)
            if customer_id == customer_id2:
                return True

        return False

    @pyqtSlot()
    def on_search_button_clicked(self):

        try:
            PluginUtils.run_query(self.__search_customer)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

    def __search_customer(self):

        search_term = self.search_term_edit.text().strip()
        if len(search_term) == 0:
            return

        self.registered_cust_twidget.clearContents()
        self.registered_cust_twidget.setRowCount(0)

        if self.id_rbutton.isChecked():
            count = self.session.query(MxCustomer).\
                filter(or_(MxCustomer.id_number.ilike('%{0}%'.format(search_term)),
                           MxCustomer.can.ilike('%{0}%'.format(search_term)))).count()
        else:
            count = self.session.query(MxCustomer).filter(MxCustomer.cons_name.ilike('%{0}%'.format(search_term))).count()

        self.registered_cust_twidget.setRowCount(count)

        i = 0

        if self.id_rbutton.isChecked():
            for customer in self.session.query(MxCustomer). \
                    filter(or_(MxCustomer.id_number.ilike('%{0}%'.format(search_term)),
                               MxCustomer.can.ilike('%{0}%'.format(search_term)))).order_by(MxCustomer.cons_name):

                self.__add_row(customer, i, self.registered_cust_twidget)
                i += 1
        else:
            for customer in self.session.query(MxCustomer). \
                    filter(MxCustomer.cons_name.ilike('%{0}%'.format(search_term))).order_by(MxCustomer.cons_name):

                self.__add_row(customer, i, self.registered_cust_twidget)
                i += 1

        self.registered_cust_twidget.resizeColumnsToContents()
        self.registered_cust_twidget.horizontalHeader().setStretchLastSection(True)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("Manage_Customer.htm")
