# 导包
import argparse
import cv2
import numpy as np
import imutils
from PIL import Image, ImageDraw, ImageFont
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import keras

NORM_SIZE = 32


def args_parse():
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--model", required=True, help="path to trained model model")
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    ap.add_argument("-s", "--show", required=True, action="store_true", help="show predict image", default=False)
    print(ap.parse_args())
    args = vars(ap.parse_args())
    print(args)
    args1 = {}
    args1['model'] = 'traffic_sign.model'
    args1['image'] = 'https://xghk416.oss-cn-beijing.aliyuncs.com/train/0000/00850598-c800-430e-8143-aaf5ef31f115.png'
    args1['show'] = True
    return args


def args_parse1(url):
    args = {}
    args['model'] = 'traffic_sign.model'
    args['image'] = url
    args['show'] = True
    return args


def predict(args):
    keras.backend.clear_session()
    print("loading model...")
    model = load_model(args['model'])

    print("loading image...")
    image = cv2.imread(args['image'])
    orig = image.copy()

    # 预处理
    image = cv2.resize(image, (NORM_SIZE, NORM_SIZE))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # 预测
    result = model.predict(image)[0]
    proba = np.max(result)
    label = str(np.where(result == proba)[0])
    print('label', label[1:-1])
    result = {}
    result['label'] = label[1:-1]
    # label = '向左急转弯'
    label = "{}: {:.2f}%".format(label, proba * 100)
    print(label)
    result['proba'] = str(proba * 100)[:5] + '%'
    return result
    # if args['show']:
    #     output = imutils.resize(orig, width=400)
    #     # output = change_cv2_draw(output,'ww',(10, 25), 20, (255, 0, 0))
    #     cv2.putText(output, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    #     cv2.imshow("Output", output)
    #     cv2.waitKey(0)


def change_cv2_draw(image, strs, local, sizes, colour):
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilimg = image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype("SIMYOU.TTF", sizes, encoding="utf-8")
    draw.text(local, strs, colour, font=font)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    return image


def get_predict(url):
    args = args_parse1(url)
    result = predict(args)
    return result


if __name__ == "__main__":
    args = args_parse()
    result = predict(args)
    print(result)
