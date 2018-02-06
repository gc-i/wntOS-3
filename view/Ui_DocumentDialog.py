# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/DocumentDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DocumentDialog(object):
    def setupUi(self, DocumentDialog):
        DocumentDialog.setObjectName("DocumentDialog")
        DocumentDialog.resize(369, 410)
        DocumentDialog.setMinimumSize(QtCore.QSize(369, 410))
        DocumentDialog.setMaximumSize(QtCore.QSize(369, 410))
        self.buttonBox = QtWidgets.QDialogButtonBox(DocumentDialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 370, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.filename_edit = QtWidgets.QLineEdit(DocumentDialog)
        self.filename_edit.setGeometry(QtCore.QRect(35, 40, 266, 20))
        self.filename_edit.setReadOnly(True)
        self.filename_edit.setObjectName("filename_edit")
        self.date_edit = QtWidgets.QDateEdit(DocumentDialog)
        self.date_edit.setGeometry(QtCore.QRect(35, 165, 141, 22))
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setObjectName("date_edit")
        self.note_edit = QtWidgets.QPlainTextEdit(DocumentDialog)
        self.note_edit.setGeometry(QtCore.QRect(35, 255, 266, 106))
        self.note_edit.setObjectName("note_edit")
        self.label = QtWidgets.QLabel(DocumentDialog)
        self.label.setGeometry(QtCore.QRect(35, 25, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DocumentDialog)
        self.label_2.setGeometry(QtCore.QRect(35, 105, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DocumentDialog)
        self.label_3.setGeometry(QtCore.QRect(35, 150, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(DocumentDialog)
        self.label_8.setGeometry(QtCore.QRect(35, 240, 111, 16))
        self.label_8.setObjectName("label_8")
        self.select_file_button = QtWidgets.QPushButton(DocumentDialog)
        self.select_file_button.setGeometry(QtCore.QRect(315, 38, 25, 25))
        self.select_file_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/wnt/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_file_button.setIcon(icon)
        self.select_file_button.setObjectName("select_file_button")
        self.author_cbox = QtWidgets.QComboBox(DocumentDialog)
        self.author_cbox.setGeometry(QtCore.QRect(35, 120, 266, 22))
        self.author_cbox.setEditable(True)
        self.author_cbox.setObjectName("author_cbox")
        self.label_4 = QtWidgets.QLabel(DocumentDialog)
        self.label_4.setGeometry(QtCore.QRect(35, 65, 111, 16))
        self.label_4.setObjectName("label_4")
        self.doc_no_edit = QtWidgets.QLineEdit(DocumentDialog)
        self.doc_no_edit.setGeometry(QtCore.QRect(35, 80, 266, 20))
        self.doc_no_edit.setReadOnly(False)
        self.doc_no_edit.setObjectName("doc_no_edit")
        self.doc_type_cbox = QtWidgets.QComboBox(DocumentDialog)
        self.doc_type_cbox.setGeometry(QtCore.QRect(35, 210, 266, 22))
        self.doc_type_cbox.setEditable(False)
        self.doc_type_cbox.setObjectName("doc_type_cbox")
        self.label_5 = QtWidgets.QLabel(DocumentDialog)
        self.label_5.setGeometry(QtCore.QRect(35, 195, 111, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(DocumentDialog)
        self.buttonBox.accepted.connect(DocumentDialog.accept)
        self.buttonBox.rejected.connect(DocumentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DocumentDialog)
        DocumentDialog.setTabOrder(self.filename_edit, self.select_file_button)
        DocumentDialog.setTabOrder(self.select_file_button, self.doc_no_edit)
        DocumentDialog.setTabOrder(self.doc_no_edit, self.author_cbox)
        DocumentDialog.setTabOrder(self.author_cbox, self.date_edit)
        DocumentDialog.setTabOrder(self.date_edit, self.doc_type_cbox)
        DocumentDialog.setTabOrder(self.doc_type_cbox, self.note_edit)

    def retranslateUi(self, DocumentDialog):
        _translate = QtCore.QCoreApplication.translate
        DocumentDialog.setWindowTitle(_translate("DocumentDialog", "Add / Edit Document"))
        self.date_edit.setDisplayFormat(_translate("DocumentDialog", "yyyy-MM-dd"))
        self.label.setText(_translate("DocumentDialog", "Filename"))
        self.label_2.setText(_translate("DocumentDialog", "Author"))
        self.label_3.setText(_translate("DocumentDialog", "Creation Date"))
        self.label_8.setText(_translate("DocumentDialog", "Notes"))
        self.select_file_button.setToolTip(_translate("DocumentDialog", "Select FIle To Upload"))
        self.label_4.setText(_translate("DocumentDialog", "Document Number"))
        self.label_5.setText(_translate("DocumentDialog", "Document Type"))

from . import resources_rc
