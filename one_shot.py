import tensorflow as tf
import pandas as pd
import numpy as np
import cv2
import os.path

from PIL import Image
from tensorflow.python import keras
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt

img = Image.open('images_background/Arcadian/character01/0001_02.png')
arr = np.asarray(img.getdata()).reshape(img.size)
print(arr)

i=0

arc = os.path.join("images_background")
for alphabet in os.listdir(arc):
    for characters in os.listdir(os.path.join(arc,alphabet)):
        for sub in os.listdir(os.path.join(arc,alphabet,characters)):
            print(os.path.join(arc,alphabet,characters,sub))
            i +=1
print(i)
print(type(walk))
plt.imshow(arr)
plt.show()
