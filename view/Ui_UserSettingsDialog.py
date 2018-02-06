# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/UserSettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserSettingsDialog(object):
    def setupUi(self, UserSettingsDialog):
        UserSettingsDialog.setObjectName("UserSettingsDialog")
        UserSettingsDialog.resize(400, 300)
        UserSettingsDialog.setMinimumSize(QtCore.QSize(400, 300))
        UserSettingsDialog.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/wnt/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UserSettingsDialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(UserSettingsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 260, 176, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(UserSettingsDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 376, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.network_cbox = QtWidgets.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(15, 30, 286, 22))
        self.network_cbox.setObjectName("network_cbox")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(15, 15, 136, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(UserSettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(UserSettingsDialog.accept)
        self.buttonBox.rejected.connect(UserSettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UserSettingsDialog)
        UserSettingsDialog.setTabOrder(self.tabWidget, self.network_cbox)

    def retranslateUi(self, UserSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        UserSettingsDialog.setWindowTitle(_translate("UserSettingsDialog", "User Settings"))
        self.label.setText(_translate("UserSettingsDialog", "Default Network"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("UserSettingsDialog", "General"))

from . import resources_rc
