import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('fortensor.csv')
X = dataset.iloc[:,:-1].values  #independent variable array
y = dataset.iloc[:,1].values  #dependent variable vector

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/3,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train) #actually produces the linear eqn for the data
y_pred = regressor.predict(X_test)
print("y is \n",y_pred)
