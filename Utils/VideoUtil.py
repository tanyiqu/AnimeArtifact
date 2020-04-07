from subprocess import call
import threading

player = 'D:/PotPlayer/PotPlayerMini64.exe'


def play(link):
    """
    调用potplayer播放视频
    :param link: 视频链接
    :return: None
    """
    # 开启线程播放
    t = threading.Thread(target=_play_, name='播放', args=(link,))
    t.start()
    pass


def _play_(link):
    call([player, link])
    pass
