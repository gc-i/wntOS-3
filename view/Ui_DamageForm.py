# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/DamageForm.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DamageForm(object):
    def setupUi(self, DamageForm):
        DamageForm.setObjectName("DamageForm")
        DamageForm.resize(553, 388)
        self.damage_twidget = QtWidgets.QTableWidget(DamageForm)
        self.damage_twidget.setGeometry(QtCore.QRect(15, 25, 496, 166))
        self.damage_twidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.damage_twidget.setAlternatingRowColors(True)
        self.damage_twidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.damage_twidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.damage_twidget.setObjectName("damage_twidget")
        self.damage_twidget.setColumnCount(11)
        self.damage_twidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.damage_twidget.setHorizontalHeaderItem(10, item)
        self.label_16 = QtWidgets.QLabel(DamageForm)
        self.label_16.setGeometry(QtCore.QRect(15, 10, 66, 16))
        self.label_16.setObjectName("label_16")
        self.view_maxcom_button = QtWidgets.QPushButton(DamageForm)
        self.view_maxcom_button.setGeometry(QtCore.QRect(515, 55, 25, 25))
        self.view_maxcom_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/wnt/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_maxcom_button.setIcon(icon)
        self.view_maxcom_button.setObjectName("view_maxcom_button")
        self.edit_damage_button = QtWidgets.QPushButton(DamageForm)
        self.edit_damage_button.setGeometry(QtCore.QRect(515, 25, 25, 25))
        self.edit_damage_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/wnt/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_damage_button.setIcon(icon1)
        self.edit_damage_button.setObjectName("edit_damage_button")

        self.retranslateUi(DamageForm)
        QtCore.QMetaObject.connectSlotsByName(DamageForm)
        DamageForm.setTabOrder(self.damage_twidget, self.edit_damage_button)
        DamageForm.setTabOrder(self.edit_damage_button, self.view_maxcom_button)

    def retranslateUi(self, DamageForm):
        _translate = QtCore.QCoreApplication.translate
        DamageForm.setWindowTitle(_translate("DamageForm", "Form"))
        item = self.damage_twidget.horizontalHeaderItem(0)
        item.setText(_translate("DamageForm", "Control No."))
        item = self.damage_twidget.horizontalHeaderItem(1)
        item.setText(_translate("DamageForm", "Received From"))
        item = self.damage_twidget.horizontalHeaderItem(2)
        item.setText(_translate("DamageForm", "Occurrence TS"))
        item = self.damage_twidget.horizontalHeaderItem(3)
        item.setText(_translate("DamageForm", "Registration TS"))
        item = self.damage_twidget.horizontalHeaderItem(4)
        item.setText(_translate("DamageForm", "Repair TS"))
        item = self.damage_twidget.horizontalHeaderItem(5)
        item.setText(_translate("DamageForm", "Repaired By"))
        item = self.damage_twidget.horizontalHeaderItem(6)
        item.setText(_translate("DamageForm", "Repair Task"))
        item = self.damage_twidget.horizontalHeaderItem(7)
        item.setText(_translate("DamageForm", "Type"))
        item = self.damage_twidget.horizontalHeaderItem(8)
        item.setText(_translate("DamageForm", "Cause"))
        item = self.damage_twidget.horizontalHeaderItem(9)
        item.setText(_translate("DamageForm", "Status"))
        item = self.damage_twidget.horizontalHeaderItem(10)
        item.setText(_translate("DamageForm", "Note"))
        self.label_16.setText(_translate("DamageForm", "Damages"))
        self.view_maxcom_button.setToolTip(_translate("DamageForm", "View Complaint Details at MAXCOM"))
        self.edit_damage_button.setToolTip(_translate("DamageForm", "View/Edit Damage Details"))

from . import resources_rc
