#导包
import argparse
import cv2
import numpy as np
import imutils
from PIL import Image, ImageDraw, ImageFont
from keras.models import load_model
from keras.preprocessing.image import img_to_array
NORM_SIZE = 32
def args_parse():
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--model", required=True, help="path to trained model model")
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    ap.add_argument("-s", "--show", required=True, action="store_true", help="show predict image", default=False)
    args = vars(ap.parse_args())
    return args

def predict(args):
    print("loading model...")
    model = load_model(args['model'])

    print("loading image...")
    image = cv2.imread(args['image'])
    orig = image.copy()

    #预处理
    image = cv2.resize(image,(NORM_SIZE, NORM_SIZE))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    #预测
    result = model.predict(image)[0]
    proba = np.max(result)
    label = str(np.where(result==proba)[0])
    print('label',label)
    # label = '向左急转弯'
    label = "{}: {:.2f}%".format(label, proba*100)
    print(label)

    if args['show']:
        output = imutils.resize(orig, width=400)
        print(output)
        # output = change_cv2_draw(output,'ww',(10, 25), 20, (255, 0, 0))
        cv2.putText(output, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Output", output)
        cv2.waitKey(0)


def change_cv2_draw(image,strs,local,sizes,colour):
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilimg = image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype("SIMYOU.TTF",sizes, encoding="utf-8")
    draw.text(local, strs, colour, font=font)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    return image

if __name__=="__main__":
    args = args_parse()
    predict(args)

