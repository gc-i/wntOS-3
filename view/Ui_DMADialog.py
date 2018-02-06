# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/DMADialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DMADialog(object):
    def setupUi(self, DMADialog):
        DMADialog.setObjectName("DMADialog")
        DMADialog.resize(588, 400)
        DMADialog.setMinimumSize(QtCore.QSize(588, 400))
        DMADialog.setMaximumSize(QtCore.QSize(588, 400))
        self.buttonBox = QtWidgets.QDialogButtonBox(DMADialog)
        self.buttonBox.setGeometry(QtCore.QRect(404, 350, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(DMADialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.dma_number_edit = QtWidgets.QLineEdit(self.tab)
        self.dma_number_edit.setGeometry(QtCore.QRect(30, 30, 196, 20))
        self.dma_number_edit.setObjectName("dma_number_edit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 15, 126, 16))
        self.label.setObjectName("label")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(260, 59, 126, 16))
        self.label_15.setObjectName("label_15")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(260, 14, 161, 16))
        self.label_14.setObjectName("label_14")
        self.network_cbox = QtWidgets.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(260, 74, 196, 22))
        self.network_cbox.setObjectName("network_cbox")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 126, 16))
        self.label_2.setObjectName("label_2")
        self.dma_name_edit = QtWidgets.QLineEdit(self.tab)
        self.dma_name_edit.setGeometry(QtCore.QRect(30, 75, 196, 20))
        self.dma_name_edit.setObjectName("dma_name_edit")
        self.area_edit = QtWidgets.QLineEdit(self.tab)
        self.area_edit.setGeometry(QtCore.QRect(260, 30, 196, 20))
        self.area_edit.setReadOnly(True)
        self.area_edit.setObjectName("area_edit")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(DMADialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(DMADialog.accept)
        self.buttonBox.rejected.connect(DMADialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DMADialog)
        DMADialog.setTabOrder(self.tabWidget, self.dma_number_edit)
        DMADialog.setTabOrder(self.dma_number_edit, self.dma_name_edit)
        DMADialog.setTabOrder(self.dma_name_edit, self.area_edit)
        DMADialog.setTabOrder(self.area_edit, self.network_cbox)
        DMADialog.setTabOrder(self.network_cbox, self.buttonBox)

    def retranslateUi(self, DMADialog):
        _translate = QtCore.QCoreApplication.translate
        DMADialog.setWindowTitle(_translate("DMADialog", "Add / Edit DMA"))
        self.label.setText(_translate("DMADialog", "DMA Number"))
        self.label_15.setText(_translate("DMADialog", "Network"))
        self.label_14.setText(_translate("DMADialog", "Calculated Area [km2]"))
        self.label_2.setText(_translate("DMADialog", "DMA Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DMADialog", "Description"))

from . import resources_rc
