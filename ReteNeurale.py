#Descrizione : programma per classificare le immagini

import tensorflow as tf 
from tensorflow import keras 
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from tensorflow.keras import layers
from keras.utils import to_categorical
import numpy as np 
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
from keras.datasets import cifar10


