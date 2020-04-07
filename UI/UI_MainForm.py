# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(1200, 880)
        self.gridLayout_2 = QtWidgets.QGridLayout(mainForm)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.browser = QWebEngineView(mainForm)
        self.browser.setMinimumSize(QtCore.QSize(0, 500))
        self.browser.setMaximumSize(QtCore.QSize(16777215, 800))
        self.browser.setObjectName("browser")
        self.gridLayout_2.addWidget(self.browser, 1, 0, 1, 2)
        self.console_secondary = QtWidgets.QTextEdit(mainForm)
        self.console_secondary.setMinimumSize(QtCore.QSize(0, 190))
        self.console_secondary.setMaximumSize(QtCore.QSize(16777215, 190))
        self.console_secondary.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"微软雅黑\";")
        self.console_secondary.setObjectName("console_secondary")
        self.gridLayout_2.addWidget(self.console_secondary, 5, 1, 1, 1)
        self.console_main = QtWidgets.QTextEdit(mainForm)
        self.console_main.setMinimumSize(QtCore.QSize(0, 190))
        self.console_main.setMaximumSize(QtCore.QSize(16777215, 190))
        self.console_main.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"微软雅黑\";")
        self.console_main.setObjectName("console_main")
        self.gridLayout_2.addWidget(self.console_main, 5, 0, 1, 1)
        self.widgetBar = QtWidgets.QWidget(mainForm)
        self.widgetBar.setMinimumSize(QtCore.QSize(0, 30))
        self.widgetBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widgetBar.setObjectName("widgetBar")
        self.gridLayout = QtWidgets.QGridLayout(self.widgetBar)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnBack = QtWidgets.QPushButton(self.widgetBar)
        self.btnBack.setMinimumSize(QtCore.QSize(0, 30))
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 0, 3, 1, 1)
        self.urlBar = QtWidgets.QLineEdit(self.widgetBar)
        self.urlBar.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.urlBar.setText("")
        self.urlBar.setReadOnly(True)
        self.urlBar.setObjectName("urlBar")
        self.gridLayout.addWidget(self.urlBar, 0, 1, 1, 1)
        self.btnCopyLink = QtWidgets.QPushButton(self.widgetBar)
        self.btnCopyLink.setMinimumSize(QtCore.QSize(0, 30))
        self.btnCopyLink.setObjectName("btnCopyLink")
        self.gridLayout.addWidget(self.btnCopyLink, 0, 0, 1, 1)
        self.btnHome = QtWidgets.QPushButton(self.widgetBar)
        self.btnHome.setMinimumSize(QtCore.QSize(0, 30))
        self.btnHome.setObjectName("btnHome")
        self.gridLayout.addWidget(self.btnHome, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widgetBar, 0, 0, 1, 2)
        self.widgetTools = QtWidgets.QWidget(mainForm)
        self.widgetTools.setMinimumSize(QtCore.QSize(0, 30))
        self.widgetTools.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widgetTools.setStyleSheet("")
        self.widgetTools.setObjectName("widgetTools")
        self.btnGetAllLinks = QtWidgets.QPushButton(self.widgetTools)
        self.btnGetAllLinks.setGeometry(QtCore.QRect(0, 0, 75, 30))
        self.btnGetAllLinks.setMinimumSize(QtCore.QSize(0, 30))
        self.btnGetAllLinks.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btnGetAllLinks.setObjectName("btnGetAllLinks")
        self.btnAbout = QtWidgets.QPushButton(self.widgetTools)
        self.btnAbout.setGeometry(QtCore.QRect(75, 0, 75, 30))
        self.btnAbout.setMinimumSize(QtCore.QSize(0, 30))
        self.btnAbout.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btnAbout.setObjectName("btnAbout")
        self.gridLayout_2.addWidget(self.widgetTools, 2, 0, 1, 2)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "看番神器 V1.0"))
        self.console_main.setHtml(_translate("mainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnBack.setText(_translate("mainForm", "返回"))
        self.btnCopyLink.setText(_translate("mainForm", "复制链接"))
        self.btnHome.setText(_translate("mainForm", "主页"))
        self.btnGetAllLinks.setText(_translate("mainForm", "抓取链接"))
        self.btnAbout.setText(_translate("mainForm", "关于"))
