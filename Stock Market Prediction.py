from neuralprophet import NeuralProphet
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stock_symbol = '005935.KS' #samsung stocks data
start_date='2019-01-01'
end_date= '2023-01-01'

stock_data=yf.download(stock_symbol,start=start_date,end=end_date)

stock_data.to_csv('stock_data.csv')
stocks=pd.read_csv('stock_data.csv')
print(stocks.dtypes)
stocks['Date']=pd.to_datetime(stocks['Date'])
print(stocks.dtypes)

stock=stocks[['Date','Close']]
stock.columns=['ds','y']
print(stock.head())

plt.plot(stock['ds'],stock['y'],c='g')
print(plt.show())

model=NeuralProphet()
model.fit(stock)

future=model.make_future_dataframe(stock,periods=300)
forecast=model.predict(future)
print(forecast.head())

plt.plot(forecast['ds'],forecast['yhat1'],c='g')