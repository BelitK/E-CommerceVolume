#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fbprophet import Prophet
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot
#univariate


# In[2]:


turkey = pd.read_excel("TurkeyData3.xls",header=0)


# In[3]:


turkey.columns = ['ds', 'y']
turkey
turkey['ds']= pd.to_datetime(turkey['ds'])


# In[4]:


model = Prophet(growth='linear',uncertainty_samples=10,n_changepoints=50)


# In[5]:


model.fit(turkey)


# In[6]:


# define the period for which we want a prediction
future = list()
while True:
    date_in = input("enter year or enter (q)uit" )
    if date_in =="q":
        break
    for i in range(1,12,3):
        date = "{0}-{1}".format(date_in,i)
        future.append([date])
    print(future)
print(future)
future = DataFrame(future)
future.columns = ['ds']
future['ds']= pd.to_datetime(future['ds'])
# use the model to make a forecast
forecast = model.predict(future)
# summarize the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
# plot forecast

model.plot(forecast)
pyplot.scatter(forecast['ds'],forecast['yhat'])
pyplot.show()


# In[7]:


# create test dataset, in quarters length
train = turkey.drop(turkey.index[:-18])
print(train)
model.plot_components(forecast)

# In[9]:
from fbprophet.plot import plot_cross_validation_metric
from sklearn.metrics import mean_absolute_error, mean_squared_log_error,classification_report
# MAE hesaplama
y_true = turkey['y'][-len(future):].values
y_pred = forecast['yhat'].values
mae = mean_absolute_error(y_true, y_pred)
loss = mean_squared_log_error(y_true,y_pred)
print("loss score",loss)
print('MAE: %.3f' % mae)
#print(classification_report(y_true,y_pred))
plot_cross_validation_metric()


# In[10]:


# plot expected vs actual
pyplot.plot(y_true, label='Actual')
pyplot.plot(y_pred, label='Predicted')
pyplot.legend()
pyplot.show()


# In[11]:


from fbprophet.plot import plot_plotly, plot_components_plotly

plot_plotly(model, forecast)


# In[12]:


plot_components_plotly(model, forecast)


# In[ ]:




