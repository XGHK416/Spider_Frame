import requests


def download_img(img_url,pic_name):
    # r = requests.get(img_url)
    # with open('./spider_pic/'+pic_name, 'wb') as f:
    #     f.write(r.content)
        try:
            if img_url is not None:
                pic = requests.get(img_url, timeout=7)
            else:
                pass
        except BaseException:
            print('错误，当前图片无法下载')
            pass
        else:
            string = './spider_pic/' + pic_name
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()

if __name__ == '__main__':
    download_img("https://tse4-mm.cn.bing.net/th?id=OIP.YPe_HjMdSy-aEoBYR0kzHwHaGN&w=256&h=215&c=7&o=5&pid=1.7","123")