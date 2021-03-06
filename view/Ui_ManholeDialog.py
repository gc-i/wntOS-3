# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/ManholeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManholeDialog(object):
    def setupUi(self, ManholeDialog):
        ManholeDialog.setObjectName("ManholeDialog")
        ManholeDialog.resize(588, 450)
        ManholeDialog.setMinimumSize(QtCore.QSize(588, 450))
        ManholeDialog.setMaximumSize(QtCore.QSize(588, 480))
        self.buttonBox = QtWidgets.QDialogButtonBox(ManholeDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 400, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(ManholeDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.inspection_intervall_sbox = QtWidgets.QDoubleSpinBox(self.tab)
        self.inspection_intervall_sbox.setGeometry(QtCore.QRect(20, 115, 196, 22))
        self.inspection_intervall_sbox.setObjectName("inspection_intervall_sbox")
        self.installation_date_edit = QtWidgets.QDateEdit(self.tab)
        self.installation_date_edit.setEnabled(False)
        self.installation_date_edit.setGeometry(QtCore.QRect(45, 75, 171, 22))
        self.installation_date_edit.setCalendarPopup(True)
        self.installation_date_edit.setObjectName("installation_date_edit")
        self.installation_date_chbox = QtWidgets.QCheckBox(self.tab)
        self.installation_date_chbox.setGeometry(QtCore.QRect(20, 80, 26, 17))
        self.installation_date_chbox.setText("")
        self.installation_date_chbox.setObjectName("installation_date_chbox")
        self.manhole_no_edit = QtWidgets.QLineEdit(self.tab)
        self.manhole_no_edit.setGeometry(QtCore.QRect(20, 30, 196, 20))
        self.manhole_no_edit.setObjectName("manhole_no_edit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 126, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 126, 16))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 15, 126, 16))
        self.label.setObjectName("label")
        self.inspection_intervall_unit_cbox = QtWidgets.QComboBox(self.tab)
        self.inspection_intervall_unit_cbox.setGeometry(QtCore.QRect(20, 160, 196, 22))
        self.inspection_intervall_unit_cbox.setObjectName("inspection_intervall_unit_cbox")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 145, 126, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 235, 126, 16))
        self.label_7.setObjectName("label_7")
        self.operating_state_cbox = QtWidgets.QComboBox(self.tab)
        self.operating_state_cbox.setGeometry(QtCore.QRect(20, 250, 196, 22))
        self.operating_state_cbox.setObjectName("operating_state_cbox")
        self.status_change_date_edit = QtWidgets.QDateEdit(self.tab)
        self.status_change_date_edit.setEnabled(False)
        self.status_change_date_edit.setGeometry(QtCore.QRect(45, 300, 171, 22))
        self.status_change_date_edit.setCalendarPopup(True)
        self.status_change_date_edit.setObjectName("status_change_date_edit")
        self.status_change_date_chbox = QtWidgets.QCheckBox(self.tab)
        self.status_change_date_chbox.setGeometry(QtCore.QRect(20, 305, 26, 17))
        self.status_change_date_chbox.setText("")
        self.status_change_date_chbox.setObjectName("status_change_date_chbox")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 285, 126, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(270, 15, 126, 16))
        self.label_9.setObjectName("label_9")
        self.purpose_cbox = QtWidgets.QComboBox(self.tab)
        self.purpose_cbox.setGeometry(QtCore.QRect(270, 30, 196, 22))
        self.purpose_cbox.setObjectName("purpose_cbox")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(270, 60, 126, 16))
        self.label_10.setObjectName("label_10")
        self.construction_type_cbox = QtWidgets.QComboBox(self.tab)
        self.construction_type_cbox.setGeometry(QtCore.QRect(270, 75, 196, 22))
        self.construction_type_cbox.setObjectName("construction_type_cbox")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(270, 100, 126, 16))
        self.label_11.setObjectName("label_11")
        self.entry_type_cbox = QtWidgets.QComboBox(self.tab)
        self.entry_type_cbox.setGeometry(QtCore.QRect(270, 115, 196, 22))
        self.entry_type_cbox.setObjectName("entry_type_cbox")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(270, 145, 126, 16))
        self.label_12.setObjectName("label_12")
        self.location_cbox = QtWidgets.QComboBox(self.tab)
        self.location_cbox.setGeometry(QtCore.QRect(270, 160, 196, 22))
        self.location_cbox.setObjectName("location_cbox")
        self.height_sbox = QtWidgets.QDoubleSpinBox(self.tab)
        self.height_sbox.setGeometry(QtCore.QRect(270, 205, 196, 22))
        self.height_sbox.setMinimum(-100.0)
        self.height_sbox.setMaximum(2000.0)
        self.height_sbox.setObjectName("height_sbox")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(270, 190, 126, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(270, 235, 126, 16))
        self.label_15.setObjectName("label_15")
        self.network_cbox = QtWidgets.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(270, 250, 196, 22))
        self.network_cbox.setObjectName("network_cbox")
        self.date_of_last_inspection_edit = QtWidgets.QDateEdit(self.tab)
        self.date_of_last_inspection_edit.setEnabled(False)
        self.date_of_last_inspection_edit.setGeometry(QtCore.QRect(45, 205, 171, 22))
        self.date_of_last_inspection_edit.setCalendarPopup(True)
        self.date_of_last_inspection_edit.setObjectName("date_of_last_inspection_edit")
        self.date_of_last_inspection_chbox = QtWidgets.QCheckBox(self.tab)
        self.date_of_last_inspection_chbox.setGeometry(QtCore.QRect(20, 210, 26, 17))
        self.date_of_last_inspection_chbox.setText("")
        self.date_of_last_inspection_chbox.setObjectName("date_of_last_inspection_chbox")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(20, 190, 126, 16))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(ManholeDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(ManholeDialog.accept)
        self.buttonBox.rejected.connect(ManholeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ManholeDialog)
        ManholeDialog.setTabOrder(self.tabWidget, self.manhole_no_edit)
        ManholeDialog.setTabOrder(self.manhole_no_edit, self.installation_date_chbox)
        ManholeDialog.setTabOrder(self.installation_date_chbox, self.installation_date_edit)
        ManholeDialog.setTabOrder(self.installation_date_edit, self.inspection_intervall_sbox)
        ManholeDialog.setTabOrder(self.inspection_intervall_sbox, self.inspection_intervall_unit_cbox)
        ManholeDialog.setTabOrder(self.inspection_intervall_unit_cbox, self.date_of_last_inspection_chbox)
        ManholeDialog.setTabOrder(self.date_of_last_inspection_chbox, self.date_of_last_inspection_edit)
        ManholeDialog.setTabOrder(self.date_of_last_inspection_edit, self.operating_state_cbox)
        ManholeDialog.setTabOrder(self.operating_state_cbox, self.status_change_date_chbox)
        ManholeDialog.setTabOrder(self.status_change_date_chbox, self.status_change_date_edit)
        ManholeDialog.setTabOrder(self.status_change_date_edit, self.purpose_cbox)
        ManholeDialog.setTabOrder(self.purpose_cbox, self.construction_type_cbox)
        ManholeDialog.setTabOrder(self.construction_type_cbox, self.entry_type_cbox)
        ManholeDialog.setTabOrder(self.entry_type_cbox, self.location_cbox)
        ManholeDialog.setTabOrder(self.location_cbox, self.height_sbox)
        ManholeDialog.setTabOrder(self.height_sbox, self.network_cbox)

    def retranslateUi(self, ManholeDialog):
        _translate = QtCore.QCoreApplication.translate
        ManholeDialog.setWindowTitle(_translate("ManholeDialog", "Add / Edit Manhole"))
        self.installation_date_edit.setDisplayFormat(_translate("ManholeDialog", "yyyy-MM-dd"))
        self.label_3.setText(_translate("ManholeDialog", "Installation Date"))
        self.label_5.setText(_translate("ManholeDialog", "Inspection Interval"))
        self.label.setText(_translate("ManholeDialog", "Manhole Number"))
        self.label_6.setText(_translate("ManholeDialog", "Inspection Interval Unit"))
        self.label_7.setText(_translate("ManholeDialog", "Operating State"))
        self.status_change_date_edit.setDisplayFormat(_translate("ManholeDialog", "yyyy-MM-dd"))
        self.label_8.setText(_translate("ManholeDialog", "Date of Status Change"))
        self.label_9.setText(_translate("ManholeDialog", "Purpose"))
        self.label_10.setText(_translate("ManholeDialog", "Construction Type"))
        self.label_11.setText(_translate("ManholeDialog", "Entry Type"))
        self.label_12.setText(_translate("ManholeDialog", "Location"))
        self.label_14.setText(_translate("ManholeDialog", "Height [m]"))
        self.label_15.setText(_translate("ManholeDialog", "Network"))
        self.date_of_last_inspection_edit.setDisplayFormat(_translate("ManholeDialog", "yyyy-MM-dd"))
        self.label_13.setText(_translate("ManholeDialog", "Date of Last Inspection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ManholeDialog", "Description"))

from . import resources_rc
