"""
进行文本处理的工具模块
"""
import winreg
import random


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


def getIntegerDigits(num):
    """
    获取整数的位数
    :param num: 整数
    :return: 位数
    """
    t = 1
    k = 10
    while True:
        if num < k:
            return t
        else:
            t += 1
            k *= 10


if __name__ == '__main__':
    for i in range(0, 10):
        n = random.randint(1, 9999)
        print(n, getIntegerDigits(n))