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

path = os.path.join("images_background","Arcadian","character01","0001_02.png")
for sub in path:
    print(sub)
print(path)
walk = os.walk(path)
print(type(walk))
plt.imshow(arr)
plt.show()
