import re
import requests
from urllib import error
from bs4 import BeautifulSoup
import os
import time
num = 0
numPicture = 0
file = ''
strtime = ''
List = []

#睡眠函数
def sleep(mytime=''):
        time.sleep(mytime)

def recommend(url):
    Re = []
    try:
        html = requests.get(url)
    except error.HTTPError as e:
        return
    else:
        html.encoding = 'utf-8'
        bsObj = BeautifulSoup(html.text, 'html.parser')
        div = bsObj.find('div', id='topRS')
        if div is not None:
            listA = div.findAll('a')
            for i in listA:
                if i is not None:
                    Re.append(i.get_text())
        return Re


def dowmloadPicture(html, keyword,fileName):
    global num
    # time.sleep(1)
    # t =0
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    describe = re.findall('"fromPageTitle":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    count = 0
    for i in range(0, len(describe)):
        if ("?" in describe[i] or "&" in describe[i]or "合集" in describe[i]) :
            print(i)
            pic_url.pop(i - count)
            count = count + 1
    print('找到关键词:' + keyword + '的图片，即将开始下载图片...')
    print('图片总数',len(pic_url))
    for each in pic_url:
        print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(each))
        try:
            if each is not None:
                pic = requests.get(each, timeout=7)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            string = 'C:\\Users\\HJM\\Desktop\\\学习资料\\图像识别\\traffic_sign_classfication-master\\data\\train\\'+fileName + r'\\' + str('0000') + '_' + str(num) + '.png'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        print(num)
        print(numPicture)
        if num >= numPicture:
            return num
    return num

def reptile(wordList,tm):
    global numPicture
    numPicture= tm
    print('tm',tm)
    with open('./name.txt', 'w', encoding='utf-8') as file:
        for word in wordList:
            file.write(str(word)+"\n")
    test = 0
    for word in wordList:
        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
        # tot = 1
        Recommend = recommend(url)  # 记录相关推荐
        # print('经过检测%s类图片共有%d张' % (word, tot))
        k = 10000
        strtime = test + k
        file = str(strtime)[1:5]
        y = os.path.exists(file)
        if y == 1:
            print('该文件已存在，请重新输入')
            file = word + '文件夹2'
            os.makedirs('C:\\Users\\HJM\\Desktop\\\学习资料\\图像识别\\traffic_sign_classfication-master\\data\\train\\'+str(strtime)[1:5])
        else:
            os.makedirs('C:\\Users\\HJM\\Desktop\\\学习资料\\图像识别\\traffic_sign_classfication-master\\data\\train\\'+str(strtime)[1:5])
        t = 0
        tmp = url
        test = test +1
        while t < numPicture:
            try:
                url = tmp + str(t)
                result = requests.get(url, timeout=10)
                print(url)
            except error.HTTPError as e:
                print('网络错误，请调整网络后重试')
                t = t + 60
            else:
                count=dowmloadPicture(result.text, word,str(strtime)[1:5])
                t = count
        numPicture=numPicture + tm

if __name__ == '__main__':  # 主函数入口
    tm = int(input('请输入每类图片的下载数量 '))
    numPicture = tm
    line_list = []
    wordList = ['向左急转弯图标','向右急转弯图标','干路先行图标','注意信号灯图标','减速让行图标','限制宽度标志'
                ,'禁止掉头图标','禁止超车图标','禁止鸣喇叭图标','停车检查图标','禁止驶入图标','禁止机动车通行标志'
                ,'驼峰桥图标','注意危险图标','最低限速50标志','会车先行标志','人行横道图标','禁止超车图标'
                ,'禁止行人通过标志','窄桥标志','堤坝路图标','注意横风标志','注意落石图标','傍山险路图标'
                ,'过水路面标志','两侧变窄图标','双向通行图标','事故易发路段图标','人行横道标志']
    reptile(wordList,tm)

    print('当前搜索结束，感谢使用')