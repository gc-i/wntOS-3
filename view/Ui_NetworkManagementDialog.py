# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/NetworkManagementDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NetworkManagementDialog(object):
    def setupUi(self, NetworkManagementDialog):
        NetworkManagementDialog.setObjectName("NetworkManagementDialog")
        NetworkManagementDialog.resize(564, 270)
        NetworkManagementDialog.setMinimumSize(QtCore.QSize(564, 270))
        NetworkManagementDialog.setMaximumSize(QtCore.QSize(564, 270))
        NetworkManagementDialog.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/wnt/network.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NetworkManagementDialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(NetworkManagementDialog)
        self.buttonBox.setGeometry(QtCore.QRect(350, 225, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.delete_network_button = QtWidgets.QPushButton(NetworkManagementDialog)
        self.delete_network_button.setGeometry(QtCore.QRect(515, 90, 25, 25))
        self.delete_network_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/wnt/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_network_button.setIcon(icon1)
        self.delete_network_button.setObjectName("delete_network_button")
        self.edit_network_button = QtWidgets.QPushButton(NetworkManagementDialog)
        self.edit_network_button.setGeometry(QtCore.QRect(515, 60, 25, 25))
        self.edit_network_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/wnt/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_network_button.setIcon(icon2)
        self.edit_network_button.setObjectName("edit_network_button")
        self.network_twidget = QtWidgets.QTableWidget(NetworkManagementDialog)
        self.network_twidget.setGeometry(QtCore.QRect(15, 30, 496, 166))
        self.network_twidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.network_twidget.setAlternatingRowColors(True)
        self.network_twidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.network_twidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.network_twidget.setObjectName("network_twidget")
        self.network_twidget.setColumnCount(4)
        self.network_twidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.network_twidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.network_twidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.network_twidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.network_twidget.setHorizontalHeaderItem(3, item)
        self.label_16 = QtWidgets.QLabel(NetworkManagementDialog)
        self.label_16.setGeometry(QtCore.QRect(15, 15, 66, 16))
        self.label_16.setObjectName("label_16")
        self.add_network_button = QtWidgets.QPushButton(NetworkManagementDialog)
        self.add_network_button.setGeometry(QtCore.QRect(515, 30, 25, 25))
        self.add_network_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/wnt/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_network_button.setIcon(icon3)
        self.add_network_button.setObjectName("add_network_button")

        self.retranslateUi(NetworkManagementDialog)
        self.buttonBox.accepted.connect(NetworkManagementDialog.accept)
        self.buttonBox.rejected.connect(NetworkManagementDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NetworkManagementDialog)
        NetworkManagementDialog.setTabOrder(self.network_twidget, self.add_network_button)
        NetworkManagementDialog.setTabOrder(self.add_network_button, self.edit_network_button)
        NetworkManagementDialog.setTabOrder(self.edit_network_button, self.delete_network_button)

    def retranslateUi(self, NetworkManagementDialog):
        _translate = QtCore.QCoreApplication.translate
        NetworkManagementDialog.setWindowTitle(_translate("NetworkManagementDialog", "Manage Networks"))
        self.delete_network_button.setToolTip(_translate("NetworkManagementDialog", "Delete Network"))
        self.edit_network_button.setToolTip(_translate("NetworkManagementDialog", "View/Edit Network Details"))
        item = self.network_twidget.horizontalHeaderItem(0)
        item.setText(_translate("NetworkManagementDialog", "Network No."))
        item = self.network_twidget.horizontalHeaderItem(1)
        item.setText(_translate("NetworkManagementDialog", "Network Name"))
        item = self.network_twidget.horizontalHeaderItem(2)
        item.setText(_translate("NetworkManagementDialog", "Dimensioning Pressure"))
        item = self.network_twidget.horizontalHeaderItem(3)
        item.setText(_translate("NetworkManagementDialog", "Operating Pressure"))
        self.label_16.setText(_translate("NetworkManagementDialog", "Networks"))
        self.add_network_button.setToolTip(_translate("NetworkManagementDialog", "Add Network"))

from . import resources_rc
