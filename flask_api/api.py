from flask import Flask, request
import spider.Spider as sp
import algorithm.upload as upload
import algorithm.download as download

app = Flask(__name__)


# 爬取数据
@app.route('/spider')
def get_spider():
    # 获取请求参数 request.args.get('name')
    target = request.args.get('target')
    data = request.args.get('today')
    result = sp.spider(target)
    pic_list = result['pic_list']
    for index, pic in enumerate(pic_list):
        name = data + "_" + str(index) + ".png"
        # 下载图片
        download.download_img(pic, name)
        # 上传图片
        upload.oss(data + "/" + name, "./spider_pic/" + name)

    return str(result)
# @app.route('/upload_spider')
# def upload_spider():
#     pic_list = request.args.get()


# 分类
@app.route('/divider')
def do_divider():
    pic = request.args.get('pic')

    return ''


# 算法
@app.route('/algorithm')
def calculate_algorithm():
    return ''


if __name__ == '__main__':
    app.run()
