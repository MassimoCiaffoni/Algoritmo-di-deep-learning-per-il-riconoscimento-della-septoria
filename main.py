#importo le librerie utilizzate
import numpy as np 
from keras.preprocessing.image import ImageDataGenerator 
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import Activation, Flatten, Dropout, Dense


img_weight, img_height=100, 100

train_dir='data/train'
validation_data_dir='data/test'


