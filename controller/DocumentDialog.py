from builtins import bytes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ..view.Ui_DocumentDialog import *
from ..utils.PluginUtils import PluginUtils
from ..model.core_classes import CoDocument, ClTypeOfDocument
from sqlalchemy.exc import SQLAlchemyError
from ..model.WntException import *
from ..model.DatabaseHelper import *


class DocumentDialog(QDialog, Ui_DocumentDialog, DatabaseHelper):

    def __init__(self, doc_id, documented_id, documented_type, parent=None):

        super(DocumentDialog, self).__init__(parent)
        DatabaseHelper.__init__(self)
        self.setupUi(self)
        self.__doc_id = doc_id
        self.__documented_id = documented_id
        self.__documented_type = documented_type
        self.__doc_content = None
        self.date_edit.setDate(QDate.currentDate())
        self.__default_path = QDir.homePath() + QDir.separator() + "Documents"
        try:
            PluginUtils.run_query(self.__populate_author_cbox)
            PluginUtils.run_query(PluginUtils.populate_codelist_cbox, 2, self.doc_type_cbox, ClTypeOfDocument, True)
            if doc_id is not None:
                PluginUtils.run_query(self.__populate_doc_details)

        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            return

    def __populate_author_cbox(self):

        for author, in self.session.query(CoDocument.creator.distinct()).order_by(CoDocument.creator):
            self.author_cbox.addItem(author)

        self.author_cbox.setCurrentIndex(-1)

    def __populate_doc_details(self):

        co_document = self.session.query(CoDocument).get(self.__doc_id)

        self.filename_edit.setText(co_document.file_name)
        self.doc_no_edit.setText(co_document.document_number)
        self.author_cbox.setCurrentIndex(self.author_cbox.findText(co_document.creator))
        self.date_edit.setDate(PluginUtils.convert_python_date_to_qt(co_document.creation_date))
        if co_document.document_type is not None:
            self.doc_type_cbox.setCurrentIndex(self.doc_type_cbox.findData(co_document.document_type, Qt.UserRole))
        self.note_edit.setPlainText(co_document.note)
        self.__doc_content = co_document.content

    def document_id(self):

        return self.__doc_id

    def accept(self):

        if not self.__validate_user_input():
            return

        try:
            PluginUtils.run_query(self.__save_document)
        except (WntException, SQLAlchemyError) as e:
            PluginUtils.show_error(self, self.tr('Database Error'), e.args[0])
            return

        QDialog.accept(self)

    def __save_document(self):

        filename = self.filename_edit.text()
        creation_date = PluginUtils.convert_qt_date_to_python(self.date_edit.date())
        author = self.author_cbox.lineEdit().text() if len(self.author_cbox.lineEdit().text()) > 0 else None
        doc_no = self.doc_no_edit.text() if len(self.doc_no_edit.text()) > 0 else None
        doc_type = self.doc_type_cbox.itemData(self.doc_type_cbox.currentIndex(), Qt.UserRole)
        note = self.note_edit.toPlainText() if len(self.note_edit.toPlainText()) > 0 else None

        new_doc = False
        self.create_savepoint()
        try:
            if self.__doc_id is None:
                co_document = CoDocument()
                new_doc = True
            else:
                co_document = self.session.query(CoDocument).get(self.__doc_id)

            co_document.file_name = filename
            co_document.content = self.__doc_content
            co_document.creator = author
            co_document.creation_date = creation_date
            co_document.document_number = doc_no
            co_document.document_type = doc_type
            co_document.note = note
            if new_doc:
                co_document.documented_type = self.__documented_type
                co_document.documented_id = self.__documented_id
            self.session.add(co_document)

            self.__doc_id = co_document.id
            self.release_savepoint()

        except SQLAlchemyError as e:
            self.rollback_to_savepoint()
            raise e

    def __validate_user_input(self):

        self.author_cbox.lineEdit().setText(self.author_cbox.lineEdit().text().strip())
        self.doc_no_edit.setText(self.doc_no_edit.text().strip())
        self.note_edit.setPlainText(self.note_edit.toPlainText().strip())

        if len(self.filename_edit.text()) == 0:
            PluginUtils.show_message(self, self.tr('No File selected'), self.tr('Please select a document file!'))
            return False

        return True

    @pyqtSlot()
    def on_select_file_button_clicked(self):

        file_path, __ = QFileDialog.getOpenFileName(self, self.tr("Select Document (max size: 1MB)"), self.__default_path,
                                                self.tr("All Files (*.*)"))
        if len(file_path) == 0:
            return

        file = QFile(file_path)
        if not file.open(QIODevice.ReadOnly):
            return

        file_size_mb = float(QFileInfo(file_path).size()) / (1024 * 1024)
        if file_size_mb > 1:
            file.close()
            QMessageBox.information(None, self.tr("File size exceeding limit"),
                                    self.tr("The maximum permitted size of a document to "
                                            "be uploaded is 1 MB. Yours has {0:.1f} MB.").format(file_size_mb))
            return

        file_name = QFileInfo(file_path).fileName()
        self.__default_path = QFileInfo(file_path).absolutePath()
        self.__doc_content = bytes(file.readAll())
        file.close()
        self.filename_edit.setText(file_name)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_F1:
            PluginUtils.show_help("document_management.html")
