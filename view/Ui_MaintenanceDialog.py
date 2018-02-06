# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/MaintenanceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MaintenanceDialog(object):
    def setupUi(self, MaintenanceDialog):
        MaintenanceDialog.setObjectName("MaintenanceDialog")
        MaintenanceDialog.resize(588, 320)
        MaintenanceDialog.setMinimumSize(QtCore.QSize(588, 320))
        MaintenanceDialog.setMaximumSize(QtCore.QSize(588, 320))
        self.buttonBox = QtWidgets.QDialogButtonBox(MaintenanceDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 280, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(MaintenanceDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.maintenance_date_edit = QtWidgets.QDateEdit(self.tab)
        self.maintenance_date_edit.setEnabled(True)
        self.maintenance_date_edit.setGeometry(QtCore.QRect(20, 30, 196, 22))
        self.maintenance_date_edit.setCalendarPopup(True)
        self.maintenance_date_edit.setObjectName("maintenance_date_edit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 15, 126, 16))
        self.label_3.setObjectName("label_3")
        self.maintained_by_cbox = QtWidgets.QComboBox(self.tab)
        self.maintained_by_cbox.setGeometry(QtCore.QRect(20, 75, 196, 22))
        self.maintained_by_cbox.setEditable(True)
        self.maintained_by_cbox.setObjectName("maintained_by_cbox")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 126, 16))
        self.label_6.setObjectName("label_6")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(270, 15, 126, 16))
        self.label_15.setObjectName("label_15")
        self.note_edit = QtWidgets.QPlainTextEdit(self.tab)
        self.note_edit.setGeometry(QtCore.QRect(270, 30, 196, 146))
        self.note_edit.setObjectName("note_edit")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 105, 141, 16))
        self.label_7.setObjectName("label_7")
        self.maintenance_task_cbox = QtWidgets.QComboBox(self.tab)
        self.maintenance_task_cbox.setGeometry(QtCore.QRect(20, 120, 196, 22))
        self.maintenance_task_cbox.setEditable(True)
        self.maintenance_task_cbox.setObjectName("maintenance_task_cbox")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(MaintenanceDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(MaintenanceDialog.accept)
        self.buttonBox.rejected.connect(MaintenanceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MaintenanceDialog)
        MaintenanceDialog.setTabOrder(self.tabWidget, self.maintenance_date_edit)
        MaintenanceDialog.setTabOrder(self.maintenance_date_edit, self.maintained_by_cbox)
        MaintenanceDialog.setTabOrder(self.maintained_by_cbox, self.maintenance_task_cbox)
        MaintenanceDialog.setTabOrder(self.maintenance_task_cbox, self.note_edit)
        MaintenanceDialog.setTabOrder(self.note_edit, self.buttonBox)

    def retranslateUi(self, MaintenanceDialog):
        _translate = QtCore.QCoreApplication.translate
        MaintenanceDialog.setWindowTitle(_translate("MaintenanceDialog", "Add / Edit Maintenance"))
        self.maintenance_date_edit.setDisplayFormat(_translate("MaintenanceDialog", "yyyy-MM-dd"))
        self.label_3.setText(_translate("MaintenanceDialog", "Maintenance Date"))
        self.label_6.setText(_translate("MaintenanceDialog", "Maintained By"))
        self.label_15.setText(_translate("MaintenanceDialog", "Note"))
        self.label_7.setText(_translate("MaintenanceDialog", "Maintenance Task / Activity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MaintenanceDialog", "Description"))

from . import resources_rc
