from fbprophet import Prophet
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot
from SendSql import connect_Firat, commit_data

#univariate


turkey = pd.read_excel("TurkeyData3.xls",header=0)


turkey.columns = ['ds', 'y']
turkey
turkey['ds']= pd.to_datetime(turkey['ds'])


model = Prophet(growth='linear',uncertainty_samples=10,n_changepoints=50)



model.fit(turkey)


# istenilen zaman aralığının alınması
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
# model ile tahmin yapılması
forecast = model.predict(future)
# özetlendirme
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
# tahminin gösterilmesi

model.plot(forecast)
pyplot.scatter(forecast['ds'],forecast['yhat'])
pyplot.show()


# test serisi yaratılması
train = turkey.drop(turkey.index[:-18])
print(train)
model.plot_components(forecast)

from sklearn.metrics import mean_absolute_error, mean_squared_log_error,classification_report
# MAE ve hata hesaplama
y_true = turkey['y'][-len(future):].values
y_pred = forecast['yhat'].values
mae = mean_absolute_error(y_true, y_pred)
loss = mean_squared_log_error(y_true,y_pred)
print("loss score",loss)
print('MAE: %.3f' % mae)


# tahmin edilenle asıl veri karşılaştırma
pyplot.plot(y_true, label='Actual')
pyplot.plot(y_pred, label='Predicted')
pyplot.legend()
pyplot.show()


from fbprophet.plot import plot_plotly, plot_components_plotly

plot_plotly(model, forecast)


plot_components_plotly(model, forecast)
