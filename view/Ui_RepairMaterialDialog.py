# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/RepairMaterialDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RepairMaterialDialog(object):
    def setupUi(self, RepairMaterialDialog):
        RepairMaterialDialog.setObjectName("RepairMaterialDialog")
        RepairMaterialDialog.resize(300, 200)
        RepairMaterialDialog.setMinimumSize(QtCore.QSize(300, 200))
        RepairMaterialDialog.setMaximumSize(QtCore.QSize(300, 200))
        self.buttonBox = QtWidgets.QDialogButtonBox(RepairMaterialDialog)
        self.buttonBox.setGeometry(QtCore.QRect(105, 155, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.cost_sbox = QtWidgets.QDoubleSpinBox(RepairMaterialDialog)
        self.cost_sbox.setGeometry(QtCore.QRect(20, 115, 251, 22))
        self.cost_sbox.setMaximum(5000000.0)
        self.cost_sbox.setObjectName("cost_sbox")
        self.label = QtWidgets.QLabel(RepairMaterialDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 126, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(RepairMaterialDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 55, 126, 16))
        self.label_2.setObjectName("label_2")
        self.material_cbox = QtWidgets.QComboBox(RepairMaterialDialog)
        self.material_cbox.setGeometry(QtCore.QRect(20, 70, 251, 22))
        self.material_cbox.setEditable(True)
        self.material_cbox.setObjectName("material_cbox")
        self.amount_sbox = QtWidgets.QSpinBox(RepairMaterialDialog)
        self.amount_sbox.setGeometry(QtCore.QRect(20, 25, 251, 22))
        self.amount_sbox.setMinimum(1)
        self.amount_sbox.setMaximum(200)
        self.amount_sbox.setObjectName("amount_sbox")
        self.label_14 = QtWidgets.QLabel(RepairMaterialDialog)
        self.label_14.setGeometry(QtCore.QRect(20, 100, 126, 16))
        self.label_14.setObjectName("label_14")

        self.retranslateUi(RepairMaterialDialog)
        self.buttonBox.accepted.connect(RepairMaterialDialog.accept)
        self.buttonBox.rejected.connect(RepairMaterialDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RepairMaterialDialog)
        RepairMaterialDialog.setTabOrder(self.amount_sbox, self.material_cbox)
        RepairMaterialDialog.setTabOrder(self.material_cbox, self.cost_sbox)

    def retranslateUi(self, RepairMaterialDialog):
        _translate = QtCore.QCoreApplication.translate
        RepairMaterialDialog.setWindowTitle(_translate("RepairMaterialDialog", "Add / Edit Repair Material"))
        self.label.setText(_translate("RepairMaterialDialog", "Amount"))
        self.label_2.setText(_translate("RepairMaterialDialog", "Material"))
        self.label_14.setText(_translate("RepairMaterialDialog", "Total Cost [TZS]"))

from . import resources_rc
