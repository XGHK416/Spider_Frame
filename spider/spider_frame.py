# -*- coding: UTF-8 -*-

# 打开网页或请求返回html或json数据
import re
import json
from bs4 import BeautifulSoup
import spider.util as util
import requests
import spider.sql as sql


def open_url(url):
    # 设置请求头
    head = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.121Safari/537.36",
        "Cookie": "UM_distinctid=167efec6114127-0b5ca80fa5777e-b781636-1fa400-167efec611586f;__guid=74616212.3534962106793367000.1553586436247.447;joymeid=5b562df428c0d3c616f9125854603cc8;test_cookie_enable=null;CNZZDATA1274517832=1248405128-1553585977-https%253A%252F%252Fwww.baidu.com%252F%7C1553672138"
    }
    data = util.check(url, None, head=head)
    if data:
        return data
    else:
        return None


# 提取html和json中有用的数据
# json
# unicode转中文 print a.decode('unicode-escape').encode('utf-8')
def parse_data(html):
    data = json.loads(html)
    items = data.get('data').get('topicList').get('detail')
    for index, item in enumerate(items):
        url = item.get('user').get('face_url')
        print(url)
        request_download(url, index)
    return data.get('data')
    # 以下自行解析


# 下载图片
def request_download(url, index):

    r = requests.get(url,verify=True)
    with open('./image/img' + str(index) + '.jpg', 'wb') as f:
        f.write(r.content)


#  html
def parse_data_html(html, param):
    soup = BeautifulSoup(html)
    table = soup.select("#CardSelectTr tr")
    # pattern = re.compile('<a.*?href="(.*?)".*?title="(.*?)".*?>.*?<img.*?alt=".*?".*?src="(.*?dr/).*?(__.*?)".*?>',
    pattern = re.compile(
        '<a.*?href="(.*?)".*?>.*?<img.*?alt=".*?".*?src="(.*?dr/).*?(__.*?)".*?>.*?<a.*?>.*?<a.*?title="(.*?)".*?>',
        re.S)
    for charactor in table:
        type1 = charactor.get('data-param1')
        type2 = charactor.get('data-param3')
        # 明日方舟专用
        # type2 = str(type2).split(',')[0]
        if type1 or type2:
            # charactor.prettify() 格式化html，不然可能解析不到
            if pattern.findall(charactor.prettify()):
                url, profileLeft, profileRight, name = pattern.findall(charactor.prettify())[0]
                profile = profileLeft + str(70) + profileRight
                url = 'http://wiki.joyme.com' + url
                print(name, profile, type1, type2)
    # 以下自行解析


def main():
    # 网站链接
    url = 'http://appapi.joyme.com/web/appoint?platform=0&referer=&uri=block%2Fdetail&tag=46&page=1'
    html = open_url(url)
    return parse_data(html)


if __name__ == '__main__':
    main()
