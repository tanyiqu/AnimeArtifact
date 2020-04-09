# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_AboutForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.resize(387, 442)
        AboutForm.setMinimumSize(QtCore.QSize(0, 0))
        AboutForm.setMaximumSize(QtCore.QSize(450, 450))
        AboutForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logo = QtWidgets.QLabel(AboutForm)
        self.logo.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.lblAppName = QtWidgets.QLabel(AboutForm)
        self.lblAppName.setGeometry(QtCore.QRect(70, 10, 351, 41))
        self.lblAppName.setStyleSheet("font: 17pt \"微软雅黑\";")
        self.lblAppName.setObjectName("lblAppName")
        self.lblVersion_ = QtWidgets.QLabel(AboutForm)
        self.lblVersion_.setGeometry(QtCore.QRect(20, 60, 31, 21))
        self.lblVersion_.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lblVersion_.setObjectName("lblVersion_")
        self.lblAuthor_ = QtWidgets.QLabel(AboutForm)
        self.lblAuthor_.setGeometry(QtCore.QRect(20, 80, 31, 21))
        self.lblAuthor_.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lblAuthor_.setObjectName("lblAuthor_")
        self.lblVersion = QtWidgets.QLabel(AboutForm)
        self.lblVersion.setGeometry(QtCore.QRect(55, 60, 181, 21))
        self.lblVersion.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lblVersion.setObjectName("lblVersion")
        self.lblAuthor = QtWidgets.QLabel(AboutForm)
        self.lblAuthor.setGeometry(QtCore.QRect(55, 80, 311, 21))
        self.lblAuthor.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lblAuthor.setOpenExternalLinks(True)
        self.lblAuthor.setObjectName("lblAuthor")
        self.gif = QtWidgets.QLabel(AboutForm)
        self.gif.setGeometry(QtCore.QRect(0, 340, 100, 100))
        self.gif.setText("")
        self.gif.setObjectName("gif")

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "关于 看番神器"))
        self.lblAppName.setText(_translate("AboutForm", "看番神器"))
        self.lblVersion_.setText(_translate("AboutForm", "版本"))
        self.lblAuthor_.setText(_translate("AboutForm", "作者"))
        self.lblVersion.setText(_translate("AboutForm", "1.0 (2020.4.9)"))
        self.lblAuthor.setText(_translate("AboutForm", "<a href=https://tanyiqu.github.io>Tanyiqu"))
