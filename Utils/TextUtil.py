"""
进行文本处理的工具模块
"""

def QUrl_2_str(qurl):
    """
    QUrl转字符串形式的url
    :param qurl: QUrl
    :return: 字符串形式的url
    """
    currUrl = str(qurl)
    currUrl = currUrl[19:len(currUrl) - 2]
    return currUrl