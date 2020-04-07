from PyQt5.QtCore import QUrl
from UI.UI_MainForm import Ui_mainForm
import R


class MainForm(Ui_mainForm):
    """
    继承由pyuic生成的Form
    在此文件里写信号槽
    """

    def init(self):
        self.browser.load(QUrl(R.string.HOME_URL))

        pass