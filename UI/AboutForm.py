from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QMovie

from UI.UI_AboutForm import Ui_AboutForm
import R


class AboutForm(Ui_AboutForm):

    def init(self, AboutForm):
        # 设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutForm.setWindowIcon(icon)
        # 设置标题
        AboutForm.setWindowTitle('关于 ' + R.string.APP_NAME)
        # 设置版本号
        self.lblVersion.setText(R.string.VERSION)
        # 设置logo
        pix = QPixmap('resource/images/logo.png')
        self.logo.setPixmap(pix)
        self.logo.setScaledContents(True)
        # 设置动图
        movie1 = QMovie('resource/images/gif1.gif')
        movie2 = QMovie('resource/images/gif2.gif')
        self.gif_1.setMovie(movie1)
        self.gif_2.setMovie(movie2)
        self.gif_1.setScaledContents(True)
        self.gif_2.setScaledContents(True)
        movie1.start()
        movie2.start()
        pass

    pass
