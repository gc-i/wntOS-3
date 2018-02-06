# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/MaintenanceForm.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MaintenanceForm(object):
    def setupUi(self, MaintenanceForm):
        MaintenanceForm.setObjectName("MaintenanceForm")
        MaintenanceForm.resize(553, 388)
        self.delete_maintenance_button = QtWidgets.QPushButton(MaintenanceForm)
        self.delete_maintenance_button.setGeometry(QtCore.QRect(515, 85, 25, 25))
        self.delete_maintenance_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/wnt/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_maintenance_button.setIcon(icon)
        self.delete_maintenance_button.setObjectName("delete_maintenance_button")
        self.maintenance_twidget = QtWidgets.QTableWidget(MaintenanceForm)
        self.maintenance_twidget.setGeometry(QtCore.QRect(15, 25, 496, 166))
        self.maintenance_twidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.maintenance_twidget.setAlternatingRowColors(True)
        self.maintenance_twidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.maintenance_twidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.maintenance_twidget.setColumnCount(4)
        self.maintenance_twidget.setObjectName("maintenance_twidget")
        self.maintenance_twidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.maintenance_twidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.maintenance_twidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.maintenance_twidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.maintenance_twidget.setHorizontalHeaderItem(3, item)
        self.maintenance_twidget.horizontalHeader().setVisible(True)
        self.maintenance_twidget.horizontalHeader().setDefaultSectionSize(110)
        self.maintenance_twidget.horizontalHeader().setMinimumSectionSize(35)
        self.add_maintenance_button = QtWidgets.QPushButton(MaintenanceForm)
        self.add_maintenance_button.setGeometry(QtCore.QRect(515, 25, 25, 25))
        self.add_maintenance_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/wnt/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_maintenance_button.setIcon(icon1)
        self.add_maintenance_button.setObjectName("add_maintenance_button")
        self.label_16 = QtWidgets.QLabel(MaintenanceForm)
        self.label_16.setGeometry(QtCore.QRect(15, 10, 66, 16))
        self.label_16.setObjectName("label_16")
        self.edit_maintenance_button = QtWidgets.QPushButton(MaintenanceForm)
        self.edit_maintenance_button.setGeometry(QtCore.QRect(515, 55, 25, 25))
        self.edit_maintenance_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/wnt/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_maintenance_button.setIcon(icon2)
        self.edit_maintenance_button.setObjectName("edit_maintenance_button")

        self.retranslateUi(MaintenanceForm)
        QtCore.QMetaObject.connectSlotsByName(MaintenanceForm)
        MaintenanceForm.setTabOrder(self.maintenance_twidget, self.add_maintenance_button)
        MaintenanceForm.setTabOrder(self.add_maintenance_button, self.edit_maintenance_button)
        MaintenanceForm.setTabOrder(self.edit_maintenance_button, self.delete_maintenance_button)

    def retranslateUi(self, MaintenanceForm):
        _translate = QtCore.QCoreApplication.translate
        MaintenanceForm.setWindowTitle(_translate("MaintenanceForm", "Form"))
        self.delete_maintenance_button.setToolTip(_translate("MaintenanceForm", "Delete Maintenance"))
        item = self.maintenance_twidget.horizontalHeaderItem(0)
        item.setText(_translate("MaintenanceForm", "Maintenance Date"))
        item = self.maintenance_twidget.horizontalHeaderItem(1)
        item.setText(_translate("MaintenanceForm", "Maintained By"))
        item = self.maintenance_twidget.horizontalHeaderItem(2)
        item.setText(_translate("MaintenanceForm", "Maintenance Task"))
        item = self.maintenance_twidget.horizontalHeaderItem(3)
        item.setText(_translate("MaintenanceForm", "Note"))
        self.add_maintenance_button.setToolTip(_translate("MaintenanceForm", "Add Maintenance"))
        self.label_16.setText(_translate("MaintenanceForm", "Maintenance"))
        self.edit_maintenance_button.setToolTip(_translate("MaintenanceForm", "View/Edit Maintenance Details"))

from . import resources_rc
