from flask import Flask, request
import spider.spider_frame as sp

app = Flask(__name__)


@app.route('/')
def hello_world():
    message = request.args.get('name')
    age = request.args.get('age')
    print(message,age)
    return sp.main()


if __name__ == '__main__':
    app.run()
