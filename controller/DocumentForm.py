from __future__ import absolute_import
from PyQt5.QtWidgets import *
from builtins import range
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_DocumentForm import *
from ..model.core_classes import CoDocument
from ..model.DatabaseHelper import *
from ..utils.PluginUtils import *
from .DocumentDialog import *


class DocumentForm(QWidget, Ui_DocumentForm, DatabaseHelper):

    def __init__(self, documented_type, documented_id, parent=None):

        super(DocumentForm, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__documented_id = documented_id
        self.__documented_type = documented_type
        try:
            PluginUtils.run_query(self.__populate_document_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.add_doc_button.setEnabled(False)
            self.edit_doc_button.setEnabled(False)
            self.delete_doc_button.setEnabled(False)

    def __populate_document_twidget(self):

        self.doc_twidget.clearContents()
        self.doc_twidget.setRowCount(0)

        count = self.session.query(CoDocument).filter(CoDocument.documented_type == self.__documented_type).\
            filter(CoDocument.documented_id == self.__documented_id).count()
        self.doc_twidget.setRowCount(count)

        i = 0
        for doc_id, number, creation_date, creator, file_name, note, doc_type \
                in self.session.query(CoDocument.id, CoDocument.document_number, CoDocument.creation_date,
                                      CoDocument.creator, CoDocument.file_name, CoDocument.note,
                                      CoDocument.document_type). \
                filter(CoDocument.documented_type == self.__documented_type). \
                filter(CoDocument.documented_id == self.__documented_id).\
                order_by(CoDocument.file_name):

            item = QTableWidgetItem(number)
            item.setData(Qt.UserRole, doc_id)
            self.doc_twidget.setItem(i, 0, item)

            item = QTableWidgetItem(creation_date.isoformat())
            self.doc_twidget.setItem(i, 1, item)

            item = QTableWidgetItem(creator)
            self.doc_twidget.setItem(i, 2, item)

            item = QTableWidgetItem(file_name)
            self.doc_twidget.setItem(i, 3, item)

            if doc_type is not None:
                cl_doc_type = self.session.query(ClTypeOfDocument).get(doc_type)
                item = QTableWidgetItem(cl_doc_type.description)
                self.doc_twidget.setItem(i, 4, item)

            item = QTableWidgetItem(note)
            self.doc_twidget.setItem(i, 5, item)

            i += 1

        self.doc_twidget.resizeColumnsToContents()
        self.doc_twidget.horizontalHeader().setStretchLastSection(True)

    @pyqtSlot()
    def on_view_doc_button_clicked(self):

        if len(self.doc_twidget.selectionModel().selectedRows()) == 0:
            return

        for index in self.doc_twidget.selectionModel().selectedRows():
            row = index.row()
            doc_id = self.doc_twidget.item(row, 0).data(Qt.UserRole)

        try:
            co_document = PluginUtils.run_query(self.__retrieve_document, 2, doc_id)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        PluginUtils.open_document(co_document.file_name, co_document.content)

    def __retrieve_document(self, doc_id):

        self.create_savepoint()
        try:
            co_document = self.session.query(CoDocument).get(doc_id)
            self.release_savepoint()
        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

        return co_document

    @pyqtSlot()
    def on_add_doc_button_clicked(self):

        if self.__documented_id < 0:
            PluginUtils.show_message(self, self.tr("Asset not saved yet"),
                                     self.tr("You must save your changes to database before adding a document."))
            return

        dlg = DocumentDialog(None, self.__documented_id, self.__documented_type, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__reload_and_select_document(dlg.document_id())

    @pyqtSlot()
    def on_edit_doc_button_clicked(self):

        if len(self.doc_twidget.selectionModel().selectedRows()) == 0:
            return

        for index in self.doc_twidget.selectionModel().selectedRows():
            doc_id = self.doc_twidget.item(index.row(), 0).data(Qt.UserRole)

        dlg = DocumentDialog(doc_id, self.__documented_id, self.__documented_type, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__reload_and_select_document(doc_id)

    @pyqtSlot()
    def on_delete_doc_button_clicked(self):

        if len(self.doc_twidget.selectionModel().selectedRows()) == 0:
            return

        if QMessageBox.No == QMessageBox.question(self, self.tr("Delete Document"),
                                                  self.tr('Delete the selected document?'),
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No):
            return

        for index in self.doc_twidget.selectionModel().selectedRows():
            row = index.row()
            doc_id = self.doc_twidget.item(row, 0).data(Qt.UserRole)

        try:
            PluginUtils.run_query(self.__delete_document, 2, doc_id)
            self.doc_twidget.removeRow(row)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])

    def __delete_document(self, doc_id):

        co_document = self.session.query(CoDocument).get(doc_id)
        self.create_savepoint()
        try:
            self.session.delete(co_document)
            self.release_savepoint()
        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

    def __reload_and_select_document(self, doc_id):

        try:
            PluginUtils.run_query(self.__populate_document_twidget)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        self.__select_document(doc_id)
        self.doc_twidget.setFocus()

    def __select_document(self, doc_id):

        for row in range(self.doc_twidget.rowCount()):
            doc_id_2 = self.doc_twidget.item(row, 0).data(Qt.UserRole)
            if doc_id_2 == doc_id:
                self.doc_twidget.selectRow(row)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("document_management.html")
