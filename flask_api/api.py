from flask import Flask, request
import spider.Spider as sp
import algorithm.upload as upload
import algorithm.download as download
import algorithm.predict as predict

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
    pic_url = "https://xghk416.oss-cn-beijing.aliyuncs.com/predict/"+request.args.get('pic_name')+'.jpg'
    print(pic_url)
    download.download_img(pic_url, 'predict.png', 'predict')
    print("上传完成")
    base_url = './predict_pic/predict.png'
    print("开始预测")
    result = predict.get_predict(base_url)
    print(result)

    return str(result)


# 算法
@app.route('/algorithm')
def calculate_algorithm():
    return ''


if __name__ == '__main__':
    app.run()
