# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/DamageDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DamageDialog(object):
    def setupUi(self, DamageDialog):
        DamageDialog.setObjectName("DamageDialog")
        DamageDialog.resize(588, 570)
        DamageDialog.setMinimumSize(QtCore.QSize(588, 570))
        DamageDialog.setMaximumSize(QtCore.QSize(588, 570))
        self.buttonBox = QtWidgets.QDialogButtonBox(DamageDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 535, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(DamageDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.occurrence_date_edit = QtWidgets.QDateEdit(self.tab)
        self.occurrence_date_edit.setEnabled(False)
        self.occurrence_date_edit.setGeometry(QtCore.QRect(45, 120, 171, 22))
        self.occurrence_date_edit.setCalendarPopup(True)
        self.occurrence_date_edit.setObjectName("occurrence_date_edit")
        self.occurrence_date_chbox = QtWidgets.QCheckBox(self.tab)
        self.occurrence_date_chbox.setGeometry(QtCore.QRect(20, 125, 26, 17))
        self.occurrence_date_chbox.setText("")
        self.occurrence_date_chbox.setObjectName("occurrence_date_chbox")
        self.registration_date_edit = QtWidgets.QDateEdit(self.tab)
        self.registration_date_edit.setEnabled(True)
        self.registration_date_edit.setGeometry(QtCore.QRect(20, 165, 196, 22))
        self.registration_date_edit.setCalendarPopup(True)
        self.registration_date_edit.setObjectName("registration_date_edit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 105, 126, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 15, 231, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 126, 16))
        self.label_4.setObjectName("label_4")
        self.repaired_by_cbox = QtWidgets.QComboBox(self.tab)
        self.repaired_by_cbox.setGeometry(QtCore.QRect(20, 255, 196, 22))
        self.repaired_by_cbox.setEditable(True)
        self.repaired_by_cbox.setObjectName("repaired_by_cbox")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 126, 16))
        self.label_6.setObjectName("label_6")
        self.repair_date_edit = QtWidgets.QDateEdit(self.tab)
        self.repair_date_edit.setEnabled(False)
        self.repair_date_edit.setGeometry(QtCore.QRect(45, 210, 171, 22))
        self.repair_date_edit.setCalendarPopup(True)
        self.repair_date_edit.setObjectName("repair_date_edit")
        self.repair_date_chbox = QtWidgets.QCheckBox(self.tab)
        self.repair_date_chbox.setGeometry(QtCore.QRect(20, 215, 26, 17))
        self.repair_date_chbox.setText("")
        self.repair_date_chbox.setObjectName("repair_date_chbox")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 195, 126, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(335, 15, 126, 16))
        self.label_9.setObjectName("label_9")
        self.type_cbox = QtWidgets.QComboBox(self.tab)
        self.type_cbox.setGeometry(QtCore.QRect(335, 30, 196, 22))
        self.type_cbox.setObjectName("type_cbox")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(335, 60, 126, 16))
        self.label_10.setObjectName("label_10")
        self.cause_cbox = QtWidgets.QComboBox(self.tab)
        self.cause_cbox.setGeometry(QtCore.QRect(335, 75, 196, 22))
        self.cause_cbox.setObjectName("cause_cbox")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(335, 105, 126, 16))
        self.label_11.setObjectName("label_11")
        self.status_cbox = QtWidgets.QComboBox(self.tab)
        self.status_cbox.setGeometry(QtCore.QRect(335, 120, 196, 22))
        self.status_cbox.setObjectName("status_cbox")
        self.buffer_sbox = QtWidgets.QSpinBox(self.tab)
        self.buffer_sbox.setGeometry(QtCore.QRect(335, 165, 196, 22))
        self.buffer_sbox.setMaximum(200)
        self.buffer_sbox.setObjectName("buffer_sbox")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(335, 150, 126, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(335, 195, 126, 16))
        self.label_15.setObjectName("label_15")
        self.note_edit = QtWidgets.QPlainTextEdit(self.tab)
        self.note_edit.setGeometry(QtCore.QRect(335, 210, 196, 146))
        self.note_edit.setObjectName("note_edit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 126, 16))
        self.label_2.setObjectName("label_2")
        self.received_from_cbox = QtWidgets.QComboBox(self.tab)
        self.received_from_cbox.setGeometry(QtCore.QRect(20, 75, 196, 22))
        self.received_from_cbox.setEditable(True)
        self.received_from_cbox.setObjectName("received_from_cbox")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 285, 126, 16))
        self.label_7.setObjectName("label_7")
        self.repair_task_cbox = QtWidgets.QComboBox(self.tab)
        self.repair_task_cbox.setGeometry(QtCore.QRect(20, 300, 196, 22))
        self.repair_task_cbox.setEditable(True)
        self.repair_task_cbox.setObjectName("repair_task_cbox")
        self.verify_button = QtWidgets.QPushButton(self.tab)
        self.verify_button.setGeometry(QtCore.QRect(160, 29, 25, 25))
        self.verify_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/wnt/verify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.verify_button.setIcon(icon)
        self.verify_button.setObjectName("verify_button")
        self.control_no_sbox = QtWidgets.QSpinBox(self.tab)
        self.control_no_sbox.setGeometry(QtCore.QRect(20, 30, 131, 22))
        self.control_no_sbox.setMinimum(-1)
        self.control_no_sbox.setMaximum(8000000)
        self.control_no_sbox.setProperty("value", -1)
        self.control_no_sbox.setObjectName("control_no_sbox")
        self.damaged_asset_twidget = QtWidgets.QTableWidget(self.tab)
        self.damaged_asset_twidget.setGeometry(QtCore.QRect(20, 345, 256, 121))
        self.damaged_asset_twidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.damaged_asset_twidget.setAlternatingRowColors(True)
        self.damaged_asset_twidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.damaged_asset_twidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.damaged_asset_twidget.setObjectName("damaged_asset_twidget")
        self.damaged_asset_twidget.setColumnCount(3)
        self.damaged_asset_twidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.damaged_asset_twidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.damaged_asset_twidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.damaged_asset_twidget.setHorizontalHeaderItem(2, item)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(20, 330, 221, 16))
        self.label_12.setObjectName("label_12")
        self.set_button = QtWidgets.QPushButton(self.tab)
        self.set_button.setGeometry(QtCore.QRect(280, 345, 41, 25))
        self.set_button.setObjectName("set_button")
        self.view_maxcom_button = QtWidgets.QPushButton(self.tab)
        self.view_maxcom_button.setGeometry(QtCore.QRect(190, 29, 25, 25))
        self.view_maxcom_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/wnt/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_maxcom_button.setIcon(icon1)
        self.view_maxcom_button.setObjectName("view_maxcom_button")
        self.height_sbox = QtWidgets.QDoubleSpinBox(self.tab)
        self.height_sbox.setGeometry(QtCore.QRect(335, 380, 196, 22))
        self.height_sbox.setMinimum(-100.0)
        self.height_sbox.setMaximum(2000.0)
        self.height_sbox.setObjectName("height_sbox")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(335, 365, 126, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(335, 410, 126, 16))
        self.label_17.setObjectName("label_17")
        self.network_cbox = QtWidgets.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(335, 425, 196, 22))
        self.network_cbox.setObjectName("network_cbox")
        self.warning_label = QtWidgets.QLabel(self.tab)
        self.warning_label.setGeometry(QtCore.QRect(20, 470, 256, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.warning_label.setFont(font)
        self.warning_label.setObjectName("warning_label")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(DamageDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(DamageDialog.accept)
        self.buttonBox.rejected.connect(DamageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DamageDialog)
        DamageDialog.setTabOrder(self.tabWidget, self.control_no_sbox)
        DamageDialog.setTabOrder(self.control_no_sbox, self.verify_button)
        DamageDialog.setTabOrder(self.verify_button, self.view_maxcom_button)
        DamageDialog.setTabOrder(self.view_maxcom_button, self.received_from_cbox)
        DamageDialog.setTabOrder(self.received_from_cbox, self.occurrence_date_chbox)
        DamageDialog.setTabOrder(self.occurrence_date_chbox, self.occurrence_date_edit)
        DamageDialog.setTabOrder(self.occurrence_date_edit, self.registration_date_edit)
        DamageDialog.setTabOrder(self.registration_date_edit, self.repair_date_chbox)
        DamageDialog.setTabOrder(self.repair_date_chbox, self.repair_date_edit)
        DamageDialog.setTabOrder(self.repair_date_edit, self.repaired_by_cbox)
        DamageDialog.setTabOrder(self.repaired_by_cbox, self.repair_task_cbox)
        DamageDialog.setTabOrder(self.repair_task_cbox, self.damaged_asset_twidget)
        DamageDialog.setTabOrder(self.damaged_asset_twidget, self.set_button)
        DamageDialog.setTabOrder(self.set_button, self.type_cbox)
        DamageDialog.setTabOrder(self.type_cbox, self.cause_cbox)
        DamageDialog.setTabOrder(self.cause_cbox, self.status_cbox)
        DamageDialog.setTabOrder(self.status_cbox, self.buffer_sbox)
        DamageDialog.setTabOrder(self.buffer_sbox, self.note_edit)
        DamageDialog.setTabOrder(self.note_edit, self.height_sbox)
        DamageDialog.setTabOrder(self.height_sbox, self.network_cbox)
        DamageDialog.setTabOrder(self.network_cbox, self.buttonBox)

    def retranslateUi(self, DamageDialog):
        _translate = QtCore.QCoreApplication.translate
        DamageDialog.setWindowTitle(_translate("DamageDialog", "Add / Edit Damage"))
        self.occurrence_date_edit.setDisplayFormat(_translate("DamageDialog", "yyyy-MM-dd"))
        self.registration_date_edit.setDisplayFormat(_translate("DamageDialog", "yyyy-MM-dd"))
        self.label_3.setText(_translate("DamageDialog", "Occurrence Date"))
        self.label.setText(_translate("DamageDialog", "Complaint Control No. (from MAXCOM)"))
        self.label_4.setText(_translate("DamageDialog", "Registration Date"))
        self.label_6.setText(_translate("DamageDialog", "Repaired By"))
        self.repair_date_edit.setDisplayFormat(_translate("DamageDialog", "yyyy-MM-dd"))
        self.label_8.setText(_translate("DamageDialog", "Repair Date"))
        self.label_9.setText(_translate("DamageDialog", "Type"))
        self.label_10.setText(_translate("DamageDialog", "Cause"))
        self.label_11.setText(_translate("DamageDialog", "Status"))
        self.label_14.setText(_translate("DamageDialog", "Buffer [m]"))
        self.label_15.setText(_translate("DamageDialog", "Note"))
        self.label_2.setText(_translate("DamageDialog", "Received From"))
        self.label_7.setText(_translate("DamageDialog", "Repair Task / Activity"))
        self.verify_button.setToolTip(_translate("DamageDialog", "Verify Control Number"))
        item = self.damaged_asset_twidget.horizontalHeaderItem(0)
        item.setText(_translate("DamageDialog", "Asset Type"))
        item = self.damaged_asset_twidget.horizontalHeaderItem(1)
        item.setText(_translate("DamageDialog", "Asset ID"))
        item = self.damaged_asset_twidget.horizontalHeaderItem(2)
        item.setText(_translate("DamageDialog", "Dist [m]"))
        self.label_12.setText(_translate("DamageDialog", "Set Damaged Asset"))
        self.set_button.setToolTip(_translate("DamageDialog", "Verify Control Number"))
        self.set_button.setText(_translate("DamageDialog", "Set"))
        self.view_maxcom_button.setToolTip(_translate("DamageDialog", "View Complaint Details at MAXCOM"))
        self.label_16.setText(_translate("DamageDialog", "Height [m]"))
        self.label_17.setText(_translate("DamageDialog", "Network"))
        self.warning_label.setText(_translate("DamageDialog", "Warning"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DamageDialog", "Description"))

from . import resources_rc
