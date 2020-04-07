import threading
import time

import win32con
import win32clipboard as wc
import re
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QTextCursor

import R
from Utils import TextUtil, CrawlUtil
from UI.UI_MainForm import Ui_mainForm


class MainForm(Ui_mainForm):
    """
    继承由pyuic生成的Form
    在此文件里写信号槽
    """

    HtmlSrc = ''            # 番剧html的源码
    episodeName = '番名'    # 番名
    episodeNum = 10         # 总集数
    episodeDir = {}         # 第几集:集数名
    episodePath = '/acg/2130/'    # 番剧编号
    jsSrc = ''              # 番剧js源码
    jsonLinkDir = {}        # 字典：{第几集 : json文件链接}

    def init(self):
        self.simpleLog(R.string.WELCOME)
        self.simpleLog(R.string.TIPS)
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
        :param msg: 信息
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
        :param msg: 信息
        :return: None
        """
        msg = msg.strip()
        self.console_main.append(msg)
        cursor = self.console_main.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.console_main.setTextCursor(cursor)
        pass

    def safeLog(self, msg):
        # 在副console打印含有时间信息的日志
        # msg = msg.strip()
        # 获取时间
        t = time.strftime('%H:%M:%S', time.localtime())
        msg = t + ' ' + msg
        # 使用append追加可能某一行不显示的bug
        self.console_secondary.append(msg)
        # print(msg)
        cursor = self.console_secondary.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.console_secondary.setTextCursor(cursor)
        pass

    def url_changed(self):
        currUrl = TextUtil.QUrl_2_str(self.browser.url())
        self.urlBar.setText(currUrl)
        if currUrl == R.string.HOME_URL:
            self.log('进入主页')
            pass

        # 首先有两种链接：
        # 第一种：
        # http://susudm.com/acg/2130/
        # http://fcdm.in/acg/2130/              出现这种形式的链接 为可以爬取所有视频链接的
        # 第二种：
        # http://susudm.com/acg/2130/1.html
        # http://fcdm.in/acg/2130/1.html        出现这种形式的链接 为可以调用potplayer播放的
        reg1 = r'http://.*?/.*?/([1-9]\d*)/$'           # 匹配第一种
        reg2 = r'http://.*?/.*?/[1-9]\d*/(.*?).html$'   # 匹配第二种
        if re.match(reg1, currUrl):
            # 开启线程执行
            t = threading.Thread(target=self.do_reg1, name='', args=(currUrl,))
            t.start()
            return
        if re.match(reg2, currUrl):
            # 开启线程执行
            t = threading.Thread(target=self.do_reg2, name='')
            t.start()
            pass
        pass

    def do_reg1(self, url):
        """
        此函数被一个线程调用
        后台执行获取番剧一些信息等操作
        :param url: 番剧的链接
        :return: None
        """
        self.safeLog('进入链接：{}'.format(url))
        self.safeLog('正在获取此番剧信息... 请耐心等待获取信息完毕后再点击观看！')
        self.safeLog('......')
        # 下载源码
        self.HtmlSrc = CrawlUtil.getHtmlSrc(url)
        # print(self.HtmlSrc)
        # 获取番名
        self.episodeName = CrawlUtil.getEpisodeName(self.HtmlSrc)
        self.safeLog('正在访问：【{}】'.format(self.episodeName))
        # 获取番剧路径
        self.episodePath = CrawlUtil.getEpisodePath(url)
        # print(self.episodePath)
        # 获取集数名的dir
        self.episodeDir = CrawlUtil.getEpisodeDir(self.HtmlSrc, self.episodePath)
        # print(self.episodeDir)
        # 获取总集数
        self.episodeNum = len(self.episodeDir)
        self.safeLog('总集数：{}'.format(self.episodeNum))

        # 如果集数过多，就打印进度信息
        if self.episodeNum > 20:
            self.safeLog('当前番剧集数过多！请耐心等待！')

            pass

        # 获取改番剧js文件的源码，后期找每一集的链接用
        self.jsSrc = CrawlUtil.getJsSrc(url)
        # print(self.jsSrc)
        # 获取 {集数:每一集的json文件}字典
        self.jsonLinkDir = CrawlUtil.getJsonLinkDir(self.jsSrc, self.episodeNum)
        # print(self.jsonLinkDir)
        # self.safeLog('获取完毕：')
        # self.safeLog('正在访问：【{}】 总集数：{}'.format(self.episodeName, self.episodeNum))
        self.safeLog('【提示】可以爬取此页面所有下载链接！！请点击【抓取链接】按钮进行此操作！！')
        self.safeLog('获取完毕!')
        pass

    def do_reg2(self):
        print(self.episodeNum)
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