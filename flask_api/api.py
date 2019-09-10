from flask import Flask, request
import spider.Spider as sp

app = Flask(__name__)


@app.route('/spider')
def get_spider():
    # 获取请求参数 request.args.get('name')
    param = request.args.get('target')
    print(param)
    return sp.spider(param)


if __name__ == '__main__':
    app.run()