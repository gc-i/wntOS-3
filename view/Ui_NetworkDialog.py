# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/NetworkDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NetworkDialog(object):
    def setupUi(self, NetworkDialog):
        NetworkDialog.setObjectName("NetworkDialog")
        NetworkDialog.resize(588, 480)
        NetworkDialog.setMinimumSize(QtCore.QSize(588, 480))
        NetworkDialog.setMaximumSize(QtCore.QSize(588, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/wnt/network.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NetworkDialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(NetworkDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 440, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(NetworkDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.network_no_edit = QtWidgets.QLineEdit(self.tab)
        self.network_no_edit.setGeometry(QtCore.QRect(20, 30, 196, 20))
        self.network_no_edit.setObjectName("network_no_edit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 15, 126, 16))
        self.label.setObjectName("label")
        self.dim_pressure_cbox = QtWidgets.QComboBox(self.tab)
        self.dim_pressure_cbox.setGeometry(QtCore.QRect(255, 30, 196, 22))
        self.dim_pressure_cbox.setObjectName("dim_pressure_cbox")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(255, 15, 126, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(255, 60, 126, 16))
        self.label_7.setObjectName("label_7")
        self.op_pressure_cbox = QtWidgets.QComboBox(self.tab)
        self.op_pressure_cbox.setGeometry(QtCore.QRect(255, 75, 196, 22))
        self.op_pressure_cbox.setObjectName("op_pressure_cbox")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 126, 16))
        self.label_2.setObjectName("label_2")
        self.network_name_edit = QtWidgets.QLineEdit(self.tab)
        self.network_name_edit.setGeometry(QtCore.QRect(20, 75, 196, 20))
        self.network_name_edit.setObjectName("network_name_edit")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(NetworkDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(NetworkDialog.accept)
        self.buttonBox.rejected.connect(NetworkDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NetworkDialog)
        NetworkDialog.setTabOrder(self.network_no_edit, self.network_name_edit)
        NetworkDialog.setTabOrder(self.network_name_edit, self.dim_pressure_cbox)
        NetworkDialog.setTabOrder(self.dim_pressure_cbox, self.op_pressure_cbox)
        NetworkDialog.setTabOrder(self.op_pressure_cbox, self.tabWidget)

    def retranslateUi(self, NetworkDialog):
        _translate = QtCore.QCoreApplication.translate
        NetworkDialog.setWindowTitle(_translate("NetworkDialog", "Add / Edit Network"))
        self.label.setText(_translate("NetworkDialog", "Network Number"))
        self.label_6.setText(_translate("NetworkDialog", "Dimensioning Pressure"))
        self.label_7.setText(_translate("NetworkDialog", "Operating Pressure"))
        self.label_2.setText(_translate("NetworkDialog", "Network Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("NetworkDialog", "Description"))

from . import resources_rc
