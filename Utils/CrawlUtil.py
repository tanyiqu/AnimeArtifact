"""
爬取步骤
1.根据源链接，爬取网页源码，顺便判断有多少个分集
2.根据源码，得到存有播放链接的js文件
3.根据js文件和集数，拼接存有播放链接的json文件地址
4.用适配好的headers访问json文件，拿到真实视频播放链接

详细步骤
根据链接 url http://susudm.com/acg/2130/
获取源码    url --> src
获取path    url --> path：/acg/2130/
获取集数    src --> num
获取番剧名  src --> name
"""

import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36 Edg/81.0.416.41'
}


def getHtmlSrc(url):
    """
    爬取指定url的源码
    :param url:指定url
    :return:源码
    """
    resp = requests.get(url, headers=headers)
    src = resp.content
    src = src.decode('utf-8')
    return src


def getEpisodeName(src):
    """
    获取番剧名
    :param src:源码
    :return: 番剧名
    """
    reg = '<dt class="name">(.*?)<span'
    name = re.findall(reg, src)[0]
    return name


def getEpisodePath(url):
    path = re.findall(r'http://.*?(/.*?)$', url)[0]
    return path


def getEpisodeDir(src, path):
    """
    获取总集数
    :param src: 源码
    :param path: 番剧的后缀
    :return: 字典：{第几集:每集的名字}
    """
    episodeDir = {}
    num = 1
    while True:
        # 拼接链接 /acg/2130/1.html
        episodeUrl = '%s%d.html' % (path, num)
        reg = '<a href="%s">(.*?)</a>' % episodeUrl
        result = re.search(reg, src)
        if result:
            # 匹配成功
            ename = re.findall(reg, src)[0]
            episodeDir.update({num: ename})
            pass
        else:
            # 匹配失败
            break
            pass
        num += 1
    return episodeDir


def getJsSrc(url):
    """
    获取存放 视频链接后缀 的js文件的源码
    :param url: url http://susudm.com/acg/2130/
    :return:  js源码
    """
    url = url + '1.html'
    src = requests.get(url, headers=headers).text
    reg = '</head><script type="text/javascript" src="(.*?)"></script>'
    # 获取js文件文件的链接
    jsLink = re.findall(reg, src)[0]
    print('jsLink：' + jsLink)
    # 获取js源码
    jsSrc = requests.get(jsLink, headers=headers).text
    return jsSrc


def getJsonLinkDir(jsSrc, num):
    """
    拼接存有播放链接的json文件的链接，返回{第几集:json链接}
    :param jsSrc: js源码
    :param num:  集数
    :return: 字典 {第几集:json链接}
    """
    jsonLinkDir = {}
    # 依次拼接链接
    for i in range(1, num + 1):
        reg1 = r'playarr.*?\[%d\]="(.*?),' % i  # 原来的正则，尝试匹配
        # playarr_1[1] = "1006_61136653f7514b4d9f5c8e828067dbbb,
        # reg2 = r'playarr.*?\[%d\]="(\S{37}),' % i
        # 先用reg2尝试匹配，如果reg2没有匹配成功，就换reg1匹配
        # temp = re.search(reg2, jsSrc)
        # if temp:
        #     suffix = re.findall(reg2, jsSrc)[0]
        # else:
        #     suffix = re.findall(reg1, jsSrc)[0]

        suffix = re.findall(reg1, jsSrc)[0]
        # print(suffix)

        jsonLink = 'http://test.1yltao.com/testapi888.php?time={}&url={}'.format(int(time.time()), suffix)
        # print(jsonLink)
        jsonLinkDir.update({i: jsonLink})
    return jsonLinkDir


def getPlayLink(jsonLink):
    # time.sleep(1)
    # print('jsonLink：' + jsonLink)
    temp_url = re.findall('url=(.*?)', jsonLink)[0]
    myheaders = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Host': 'test.1yltao.com',
        'Origin': 'http://test2.diyiwl.wang',
        'Referer': 'http://test2.diyiwl.wang/1717yun/mytest.php?url={}'.format(temp_url),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36 Edg/81.0.416.41'
    }
    s = requests.get(jsonLink, headers=myheaders).text
    s = re.findall('"url":"(.*?)"', s)[0]
    s = s.replace('\\', '')
    return s
