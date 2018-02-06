# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './view/FindFeatureDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FindFeatureDialog(object):
    def setupUi(self, FindFeatureDialog):
        FindFeatureDialog.setObjectName("FindFeatureDialog")
        FindFeatureDialog.resize(300, 285)
        FindFeatureDialog.setMinimumSize(QtCore.QSize(300, 285))
        FindFeatureDialog.setMaximumSize(QtCore.QSize(300, 285))
        FindFeatureDialog.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(FindFeatureDialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 235, 116, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.feature_lwidget = QtWidgets.QListWidget(FindFeatureDialog)
        self.feature_lwidget.setGeometry(QtCore.QRect(20, 30, 256, 192))
        self.feature_lwidget.setObjectName("feature_lwidget")
        self.list_title_label = QtWidgets.QLabel(FindFeatureDialog)
        self.list_title_label.setGeometry(QtCore.QRect(20, 15, 246, 16))
        self.list_title_label.setObjectName("list_title_label")

        self.retranslateUi(FindFeatureDialog)
        self.buttonBox.accepted.connect(FindFeatureDialog.accept)
        self.buttonBox.rejected.connect(FindFeatureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FindFeatureDialog)

    def retranslateUi(self, FindFeatureDialog):
        _translate = QtCore.QCoreApplication.translate
        FindFeatureDialog.setWindowTitle(_translate("FindFeatureDialog", "Find Features"))
        self.list_title_label.setText(_translate("FindFeatureDialog", "Features Found"))

