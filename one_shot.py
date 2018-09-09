import tensorflow as tf
import pandas as pd
import numpy as np
import cv2
import os.path

from PIL import Image
from tensorflow.python import keras
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt


path = 'images_background/Arcadian/character01/0001_02.png'
label_idx = path.find('.png') -7
print(label_idx)
print(path[label_idx:label_idx+4])

i=0
train_x = np.zeros((19280,105,105))
print(train_x.shape)
train_y = np.zeros((19280))

print(train_x.shape)

arc = os.path.join("images_background")
for alphabet in os.listdir(arc):
    for characters in os.listdir(os.path.join(arc,alphabet)):
        for sub in os.listdir(os.path.join(arc,alphabet,characters)):
            path = os.path.join(arc,alphabet,characters,sub)
            img = Image.open(path)
            train_x[i,:,:] = np.asarray(img.getdata()).reshape(img.size)
            train_y[i] = int(path[path.find('.png')-7:path.find('.png')-3])
            print(train_y[i])
            i +=1

plt.imshow(train_x[np.where(train_y==80)][10].reshape(105,105))
print(path)
print(int(path[path.find('.png')-7:path.find('.png')-3]))


x =10
a =1
print(train_y[0:20])
plt.imshow(train_x[10*a:10*a+x,:,:].reshape(105*x,105))
