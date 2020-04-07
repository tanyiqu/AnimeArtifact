import time

import win32con
import win32clipboard as wc
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QTextCursor

import R
from Utils import TextUtil
from UI.UI_MainForm import Ui_mainForm


class MainForm(Ui_mainForm):
    """
    继承由pyuic生成的Form
    在此文件里写信号槽
    """

    def init(self):
        self.simpleLog(R.string.WELCOME)
        self.simpleLog(R.string.TIPS)
        self.log('进入主页')
        # web
        self.browser.load(QUrl(R.string.HOME_URL))
        self.browser.urlChanged.connect(self.url_changed)
        # 复制链接
        self.btnCopyLink.clicked.connect(self.btnCopyLink_clicked)
        # 回到主页
        self.btnHome.clicked.connect(self.btnHome_clicked)
        # 返回按钮
        self.btnBack.clicked.connect(self.btnBack_clicked)
        pass

    def log(self, msg):
        """
        在主console打印含有时间信息的日志
        :return: None
        """
        msg = msg.strip()
        # 获取时间
        t = time.strftime('%H:%M:%S', time.localtime())
        self.console_main.append(t + ' ' + msg)
        cursor = self.console_main.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.console_main.setTextCursor(cursor)
        pass

    def simpleLog(self, msg):
        """
        在主console打印没有时间信息的日志
        :return: None
        """
        msg = msg.strip()
        # 获取时间
        self.console_main.append(msg)
        cursor = self.console_main.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.console_main.setTextCursor(cursor)
        pass

    def url_changed(self):
        currUrl = TextUtil.QUrl_2_str(self.browser.url())
        self.urlBar.setText(currUrl)
        pass

    def btnCopyLink_clicked(self):
        url = self.urlBar.text()
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(win32con.CF_UNICODETEXT, url)
        wc.CloseClipboard()
        pass

    def btnHome_clicked(self):
        self.browser.load(QUrl(R.string.HOME_URL))
        pass

    def btnBack_clicked(self):
        self.browser.back()
        pass