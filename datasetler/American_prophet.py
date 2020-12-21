#!/usr/bin/env python
# coding: utf-8

# In[2]:


from fbprophet import Prophet
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot
#univariate


# In[4]:


amerika = pd.read_excel("ecomretailfixed.xls",header=0)


# In[17]:


amerika.columns = ['ds', 'y']
amerika
amerika['ds']= pd.to_datetime(amerika['ds'])


# In[18]:


model = Prophet(growth='linear',uncertainty_samples=100,n_changepoints=50)
#model(mcmc.samples=1,uncertainty.samples = 1000)

# In[19]:


model.fit(amerika)


# In[30]:


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


# In[31]:


# create test dataset, in quarters length
train = amerika.drop(amerika.index[:-18])
print(train)
model.plot_components(forecast)


# In[22]:


len(forecast['yhat'].values)


# In[23]:


from sklearn.metrics import mean_absolute_error, mean_squared_log_error, balanced_accuracy_score
# calculate MAE between expected and predicted values for december
y_true = amerika['y'][-len(future):].values
y_pred = forecast['yhat'].values
mae = mean_absolute_error(y_true, y_pred)
loss = mean_squared_log_error(y_true,y_pred)
print("loss score",loss)
print('MAE: %.3f' % mae)


# In[24]:


# plot expected vs actual
pyplot.plot(y_true, label='Actual')
pyplot.plot(y_pred, label='Predicted')
pyplot.legend()
pyplot.show()


# In[25]:


from fbprophet.plot import plot_plotly, plot_components_plotly

plot_plotly(model, forecast)


# In[12]:


plot_components_plotly(model, forecast)


# In[ ]:




