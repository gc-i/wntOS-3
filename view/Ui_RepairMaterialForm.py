# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/RepairMaterialForm.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RepairMaterialForm(object):
    def setupUi(self, RepairMaterialForm):
        RepairMaterialForm.setObjectName("RepairMaterialForm")
        RepairMaterialForm.resize(554, 340)
        self.material_twidget = QtWidgets.QTableWidget(RepairMaterialForm)
        self.material_twidget.setGeometry(QtCore.QRect(15, 25, 496, 166))
        self.material_twidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.material_twidget.setAlternatingRowColors(True)
        self.material_twidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.material_twidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.material_twidget.setObjectName("material_twidget")
        self.material_twidget.setColumnCount(3)
        self.material_twidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.material_twidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.material_twidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.material_twidget.setHorizontalHeaderItem(2, item)
        self.delete_material_button = QtWidgets.QPushButton(RepairMaterialForm)
        self.delete_material_button.setGeometry(QtCore.QRect(515, 85, 25, 25))
        self.delete_material_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/wnt/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_material_button.setIcon(icon)
        self.delete_material_button.setObjectName("delete_material_button")
        self.add_material_button = QtWidgets.QPushButton(RepairMaterialForm)
        self.add_material_button.setGeometry(QtCore.QRect(515, 25, 25, 25))
        self.add_material_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/wnt/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_material_button.setIcon(icon1)
        self.add_material_button.setObjectName("add_material_button")
        self.edit_material_button = QtWidgets.QPushButton(RepairMaterialForm)
        self.edit_material_button.setGeometry(QtCore.QRect(515, 55, 25, 25))
        self.edit_material_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/wnt/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_material_button.setIcon(icon2)
        self.edit_material_button.setObjectName("edit_material_button")
        self.label_16 = QtWidgets.QLabel(RepairMaterialForm)
        self.label_16.setGeometry(QtCore.QRect(15, 10, 131, 16))
        self.label_16.setObjectName("label_16")

        self.retranslateUi(RepairMaterialForm)
        QtCore.QMetaObject.connectSlotsByName(RepairMaterialForm)

    def retranslateUi(self, RepairMaterialForm):
        _translate = QtCore.QCoreApplication.translate
        RepairMaterialForm.setWindowTitle(_translate("RepairMaterialForm", "Form"))
        item = self.material_twidget.horizontalHeaderItem(0)
        item.setText(_translate("RepairMaterialForm", "Amount"))
        item = self.material_twidget.horizontalHeaderItem(1)
        item.setText(_translate("RepairMaterialForm", "Material"))
        item = self.material_twidget.horizontalHeaderItem(2)
        item.setText(_translate("RepairMaterialForm", "Total Cost [TZS]"))
        self.delete_material_button.setToolTip(_translate("RepairMaterialForm", "Delete Material"))
        self.add_material_button.setToolTip(_translate("RepairMaterialForm", "Add Material"))
        self.edit_material_button.setToolTip(_translate("RepairMaterialForm", "View/Edit Material Details"))
        self.label_16.setText(_translate("RepairMaterialForm", "Repair Material"))

from . import resources_rc
