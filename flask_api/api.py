# -*- coding:utf-8 -*-
import os
from flask import Flask, request
import spider.Spider as sp
import algorithm.upload as upload
import algorithm.download as download
import algorithm.predict as predict
import json

app = Flask(__name__)


# 爬取数据
@app.route('/spider')
def get_spider():
    # 获取请求参数 request.args.get('name')
    target = request.args.get('target')
    data = request.args.get('today')
    result = sp.spider(target)
    pic_list = result['data']
    for index, pic in enumerate(pic_list):
        name = data + "_" + str(index) + ".png"
        # 下载图片
        download.download_img(pic, name, None, None)
        # 上传图片
        upload.oss(data + "/" + name, "./spider_pic/" + name)

    return str(result)


# @app.route('/upload_spider')
# def upload_spider():
#     pic_list = request.args.get()

@app.route('/tagging')
def get_in_train():
    pic_url = request.args.get('pic_url')
    pic_name = request.args.get('pic_name')
    pic_type = request.args.get('pic_type')
    print(pic_type,pic_url,pic_name)
    download.download_img(pic_url, pic_name, "into_train", pic_type)
    return "success"


# 分类
@app.route('/divider')
def do_divider():
    pic_url = "https://xghk416.oss-cn-beijing.aliyuncs.com/predict/" + request.args.get('pic_name') + '.jpg'
    print(pic_url)
    download.download_img(pic_url, 'predict.png', 'predict', None)
    print("上传完成")
    base_url = './predict_pic/predict.png'
    print("开始预测")
    result = predict.get_predict(base_url)

    return str(result)
#数据集分类
@app.route('/divide_train_test')
def divide_train_test():
    os.system('python ../algorithm/divide_train_test.py')
    return 'success'
# 获取准确率参数
@app.route('/get_acc')
def get_acc():
    with open('./model_acc/test.json', 'r') as f:
        data = json.load(f)
        return str(data)

# 算法
@app.route('/algorithm')
def calculate_algorithm():
    return ''


if __name__ == '__main__':
    app.run()
