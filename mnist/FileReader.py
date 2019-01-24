#coding:utf-8

import re
import os
import codecs
import struct
import numpy as np
import matplotlib.pyplot as plt


def load_mnist(filename):
    '''
    mnist包括四个文件，训练集，训练集标注，测试集，测试集标注
    训练集：60000个图片样本，每张图片大小为28X28个像素，每个像素用灰度值表示
    测试集：10000个图片样本
    '''

    path_prefix = '/mnt/d/code/python/ml/dataset/'

    path_image_suffix = '-images.idx3-ubyte'
    path_label_suffix = '-labels.idx1-ubyte'

    imgPath = path_prefix + filename + path_image_suffix
    labelPath = path_prefix + filename + path_label_suffix

    dataSet = dict()

    

    with open(imgPath,'rb') as imgFp:

        (magic_number, num, rows, cols) = struct.unpack('>IIII', imgFp.read(16))
        images = np.zeros((num, rows, cols))
        for idx in range(num):
            imgMatrix = np.fromfile(imgFp, dtype=np.uint8, count=784).reshape(rows,cols)
            images[idx] = imgMatrix
    
    with open(labelPath, 'rb') as labelFp:

        (magic_number, num) = struct.unpack('>II', labelFp.read(8))

        labels = np.fromfile(labelFp, dtype=np.uint8).reshape(num)
    
    dataSet['images'] = images
    dataSet['labels'] = labels

    return dataSet

            

if __name__ == '__main__':

    trainDataSet = load_mnist('train')

    images = trainDataSet['images']
    labels = trainDataSet['labels']

    plt.imshow(images[3324], cmap='Greys')
    plt.show()
    print labels[3324]


