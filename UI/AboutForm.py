from PyQt5.QtGui import QPixmap, QMovie

from UI.UI_AboutForm import Ui_AboutForm
import R


class AboutForm(Ui_AboutForm):

    def init(self):
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
