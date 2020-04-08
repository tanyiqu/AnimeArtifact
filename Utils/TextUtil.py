"""
进行文本处理的工具模块
"""
import winreg


def QUrl_2_str(qurl):
    """
    QUrl转字符串形式的url
    :param qurl: QUrl
    :return: 字符串形式的url
    """
    currUrl = str(qurl)
    currUrl = currUrl[19:len(currUrl) - 2]
    return currUrl


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]
