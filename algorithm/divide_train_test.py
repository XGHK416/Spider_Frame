# -*- coding:utf-8 -*-
# 将一个文件夹下图片按比例分在两个文件夹下，比例改0.7这个值即可
import os
import random
import shutil
from shutil import copy2

trainfiles_path = '../algorithm/data/datas/00'
trainfiles = os.listdir('../algorithm/data/datas/')  # （图片文件夹）
trainDir = '../algorithm/data/train/00'  # （将图片文件夹中的7份放在这个文件夹下）
validDir = '../algorithm/data/test/00'  # （将图片文件夹中的3份放在这个文件夹下）
num_child_dir = len(trainfiles)
print("num_child_dir: " + str(num_child_dir))
index_list = list(range(num_child_dir))
print(index_list)
# random.shuffle(index_list)
num = 0
# 进行子文件夹的遍历
for i in index_list:
    if len(str(i)) is 1:
        childFileDir = trainfiles_path + "0" + str(i)
        pic_trainDir = trainDir + "0" + str(i)
        pic_testDir = validDir + "0" + str(i)
    else:
        childFileDir = trainfiles_path + str(i)
        pic_trainDir = trainDir + str(i)
        pic_testDir = validDir + str(i)
    #如果子文件夹没有则创建
    if os.path.exists(pic_trainDir):
        pass
    else:os.makedirs(pic_trainDir)

    if os.path.exists(pic_testDir):
        pass
    else:os.makedirs(pic_testDir)
    # 对子文件夹下的图片扫描
    picsName = os.listdir(childFileDir)
    num_pic = len(picsName)
    print("num_pic" + str(num_pic))
    num_pic_list = list(range(num_pic))
    random.shuffle(num_pic_list)
    for j in num_pic_list:
        fileName = os.path.join(childFileDir,picsName[j])
        if j < num_pic * 0.7:
            print(str(fileName))
            copy2(fileName, pic_trainDir)
        else:
            copy2(fileName, pic_testDir)
        num += 1
