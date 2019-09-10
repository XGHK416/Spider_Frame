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
    return data.get('data')
    # 以下自行解析

#  html 必应
def parse_data_Bing(html, param):
    soup = BeautifulSoup(html)
    table = soup.select(".imgpt .iusc .mimg")
    result = []
    for i in table:
        result.append(i['src'])
    return result
    # for charactor in table:
    #     type1 = charactor.get('data-param1')
    #     type2 = charactor.get('data-param3')
    #     # 明日方舟专用
    #     # type2 = str(type2).split(',')[0]
    #     if type1 or type2:
    #         # charactor.prettify() 格式化html，不然可能解析不到
    #         if pattern.findall(charactor.prettify()):
    #             url, profileLeft, profileRight, name = pattern.findall(charactor.prettify())[0]
    #             profile = profileLeft + str(70) + profileRight
    #             url = 'http://wiki.joyme.com' + url
    #             print(name, profile, type1, type2)
    # # 以下自行解析


#Google
def parse_data_Google(html,param):
    # pattern = re.compile('<a.*?href="(.*?)".*?title="(.*?)".*?>.*?<img.*?alt=".*?".*?src="(.*?dr/).*?(__.*?)".*?>',
    pattern = re.compile(
        'src="(.*?)"',re.S)
    url_list = pattern.findall(html)
    result = []
    for i in url_list:
        result.append(i)
    return result


def spider(target):
    which_to_spide = target
    # 网站链接
    web_list = {
        "1": ["Bing","https://cn.bing.com/images/async?q=交通标志&first=0&count=35&relp=35&qft=+filterui%3aphoto-photo+filterui%3aaspect-square&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased&mmasync=1&dgState=x*0_y*0_h*0_c*5_i*36_r*7&IG=877F128F446144A4AB040EDEDDBF0EEC&SFX=2&iid=images.5632"],
        "2": ["Google","https://www.google.com/search?ei=JIh3XfXQC4fT-QaQz4KADA&tbs=itp:clipart&yv=3&q=%E4%BA%A4%E9%80%9A%E6%A0%87%E5%BF%97&tbm=isch&vet=10ahUKEwj18ujIksbkAhWHad4KHZCnAMAQuT0IQCgB.JIh3XfXQC4fT-QaQz4KADA.i&ved=0ahUKEwj18ujIksbkAhWHad4KHZCnAMAQuT0IQCgB&ijn=0&start=0&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc"]
    }
    parse = "parse_data_"
    print("1113"+which_to_spide)
    url_dict = web_list.get(which_to_spide)
    html = open_url(url_dict[1])
    parse_function = parse+url_dict[0]+"(html,None)"
    result = {"result":eval(parse_function)}
    print(type(result))
    return result


if __name__ == '__main__':
    spider(1)
