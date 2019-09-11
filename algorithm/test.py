#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  24 10:47:36 2018

@author: yxh
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

import sys
import shutil

def turnto24(path,newpath):
    files = os.listdir(path)
    print(files)
    files = np.sort(files)
    i=0
    for f in files:
        imgpath = path + f
        img=Image.open(imgpath).convert('RGB')
        dirpath = newpath
        file_name, file_extend = os.path.splitext(f)
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.png')
        img.save(dst)
for i in range(3,45):
    path1='C:/Users/HJM/Desktop/爬虫/00'
    path3 = 'C:/Users/HJM/Desktop/爬虫1/00'
    if i<10:
        i='0'+str(i)
    path2=path1+str(i)+'/'
    path3=path3+str(i)+'/'
    print(path2)
    turnto24(path2,path3)
