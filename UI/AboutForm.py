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
        AboutForm.setWindowTitle('关于 ' + R.string.APP_NAME + ' ' + R.string.VERSION)
        # 设置版本号
        self.lblVersion.setText(R.string.VERSION)
        # 设置logo
        pix = QPixmap('resource/images/logo.png')
        self.logo.setPixmap(pix)
        self.logo.setScaledContents(True)
        # 设置动图
        movie = QMovie('resource/images/gif2.gif')
        self.gif.setMovie(movie)
        self.gif.setScaledContents(True)
        movie.start()
        pass

    pass
