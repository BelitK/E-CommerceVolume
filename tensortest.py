import tensorflow as tf
import pandas as pd
from tensorflow import keras
import numpy as np

def house_model(y_new):
    xs = np.array([20.11,20.12,20.13,20.14,20.15,20.16,20.17,20.18,20.19])
    ys = np.array([100.0,150.0,200.0,250.0,300.0,350.0,400.0,450.0,500.0])
    model = tf.keras.Sequential([keras.layers.Dense(units = 2,input_shape=[1])])
    model.compile(optimizer='sgd',loss='mean_squared_error')
    model.fit(xs,ys,epochs=200)
    return model.predict(y_new)[0]

test = house_model([30.12])
print(test)