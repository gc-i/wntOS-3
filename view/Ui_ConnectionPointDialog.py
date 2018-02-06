# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/ConnectionPointDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConnectionPointDialog(object):
    def setupUi(self, ConnectionPointDialog):
        ConnectionPointDialog.setObjectName("ConnectionPointDialog")
        ConnectionPointDialog.resize(588, 360)
        ConnectionPointDialog.setMinimumSize(QtCore.QSize(588, 360))
        ConnectionPointDialog.setMaximumSize(QtCore.QSize(588, 360))
        self.buttonBox = QtWidgets.QDialogButtonBox(ConnectionPointDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 310, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(ConnectionPointDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.installation_date_edit = QtWidgets.QDateEdit(self.tab)
        self.installation_date_edit.setEnabled(False)
        self.installation_date_edit.setGeometry(QtCore.QRect(45, 120, 171, 22))
        self.installation_date_edit.setCalendarPopup(True)
        self.installation_date_edit.setObjectName("installation_date_edit")
        self.installation_length_sbox = QtWidgets.QDoubleSpinBox(self.tab)
        self.installation_length_sbox.setGeometry(QtCore.QRect(20, 75, 196, 22))
        self.installation_length_sbox.setDecimals(1)
        self.installation_length_sbox.setMaximum(500.0)
        self.installation_length_sbox.setObjectName("installation_length_sbox")
        self.installation_date_chbox = QtWidgets.QCheckBox(self.tab)
        self.installation_date_chbox.setGeometry(QtCore.QRect(20, 125, 26, 17))
        self.installation_date_chbox.setText("")
        self.installation_date_chbox.setObjectName("installation_date_chbox")
        self.conn_point_number_edit = QtWidgets.QLineEdit(self.tab)
        self.conn_point_number_edit.setGeometry(QtCore.QRect(20, 30, 196, 20))
        self.conn_point_number_edit.setObjectName("conn_point_number_edit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 126, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 105, 126, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 15, 126, 16))
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 150, 126, 16))
        self.label_10.setObjectName("label_10")
        self.conn_point_type_cbox = QtWidgets.QComboBox(self.tab)
        self.conn_point_type_cbox.setGeometry(QtCore.QRect(20, 165, 196, 22))
        self.conn_point_type_cbox.setObjectName("conn_point_type_cbox")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(270, 15, 126, 16))
        self.label_11.setObjectName("label_11")
        self.mounting_type_cbox = QtWidgets.QComboBox(self.tab)
        self.mounting_type_cbox.setGeometry(QtCore.QRect(270, 30, 196, 22))
        self.mounting_type_cbox.setObjectName("mounting_type_cbox")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(270, 60, 126, 16))
        self.label_13.setObjectName("label_13")
        self.nominal_width_cbox = QtWidgets.QComboBox(self.tab)
        self.nominal_width_cbox.setGeometry(QtCore.QRect(270, 75, 196, 22))
        self.nominal_width_cbox.setObjectName("nominal_width_cbox")
        self.height_sbox = QtWidgets.QDoubleSpinBox(self.tab)
        self.height_sbox.setGeometry(QtCore.QRect(270, 120, 196, 22))
        self.height_sbox.setMinimum(-100.0)
        self.height_sbox.setMaximum(2000.0)
        self.height_sbox.setObjectName("height_sbox")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(270, 105, 126, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(270, 150, 126, 16))
        self.label_15.setObjectName("label_15")
        self.network_cbox = QtWidgets.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(270, 165, 196, 22))
        self.network_cbox.setObjectName("network_cbox")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(ConnectionPointDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(ConnectionPointDialog.accept)
        self.buttonBox.rejected.connect(ConnectionPointDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConnectionPointDialog)
        ConnectionPointDialog.setTabOrder(self.tabWidget, self.conn_point_number_edit)
        ConnectionPointDialog.setTabOrder(self.conn_point_number_edit, self.installation_length_sbox)
        ConnectionPointDialog.setTabOrder(self.installation_length_sbox, self.installation_date_chbox)
        ConnectionPointDialog.setTabOrder(self.installation_date_chbox, self.installation_date_edit)
        ConnectionPointDialog.setTabOrder(self.installation_date_edit, self.conn_point_type_cbox)
        ConnectionPointDialog.setTabOrder(self.conn_point_type_cbox, self.mounting_type_cbox)
        ConnectionPointDialog.setTabOrder(self.mounting_type_cbox, self.nominal_width_cbox)
        ConnectionPointDialog.setTabOrder(self.nominal_width_cbox, self.height_sbox)
        ConnectionPointDialog.setTabOrder(self.height_sbox, self.network_cbox)

    def retranslateUi(self, ConnectionPointDialog):
        _translate = QtCore.QCoreApplication.translate
        ConnectionPointDialog.setWindowTitle(_translate("ConnectionPointDialog", "Add / Edit Connection Point"))
        self.installation_date_edit.setDisplayFormat(_translate("ConnectionPointDialog", "yyyy-MM-dd"))
        self.label_2.setText(_translate("ConnectionPointDialog", "Installation Length [cm]"))
        self.label_3.setText(_translate("ConnectionPointDialog", "Installation Date"))
        self.label.setText(_translate("ConnectionPointDialog", "Connection Point Number"))
        self.label_10.setText(_translate("ConnectionPointDialog", "Connection Point Type"))
        self.label_11.setText(_translate("ConnectionPointDialog", "Mounting Type"))
        self.label_13.setText(_translate("ConnectionPointDialog", "Nominal Width"))
        self.label_14.setText(_translate("ConnectionPointDialog", "Height [m]"))
        self.label_15.setText(_translate("ConnectionPointDialog", "Network"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ConnectionPointDialog", "Description"))

from . import resources_rc
