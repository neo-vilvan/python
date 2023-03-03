import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

df = pd.read_csv("G:/My Drive/gitneo/python/BTC-USD.csv", parse_dates=["Date"])
plt.plot(df["Date"],df["Close"])
#plt.show()


#Split the date and prices from the Dataset:
dates=df["Date"].to_numpy()
prices=df["Close"].to_numpy()
bitcoin_prices=df[["Date","Close"]]

#Split the Train and Test Dataset and plot them:
x_train=dates[:len(dates)-int((len(dates)*20)/100)]
x_test=dates[len(dates)-int((len(dates)*20)/100):]
y_train=prices[:len(prices)-int((len(prices)*20)/100)]
y_test=prices[len(prices)-int((len(prices)*20)/100):]

plt.scatter(x_train,y_train,s=2)
plt.scatter(x_test,y_test,s=2)

plt.figure(figsize=(10,10))
plt.bar(x_train,y_train,linewidth=100)

#Naive mode
naive_forecast = y_test[:-1]
plt.figure(figsize=(10,7))
plt.plot(x_test,y_test)
plt.scatter(x_test[1:],naive_forecast,s=2)
plt.show()

#metrics for our model
def mase(y_true,y_pred):
  mae=tf.reduce_mean(tf.abs(y_true-y_pred))
  mae_naive=tf.reduce_mean(tf.abs(y_true[1:]-y_true[:-1]))

  return mae/mae_naive

def metric(y_true,y_pred):
  mae=tf.keras.metrics.MeanAbsoluteError()
  mae.update_state(y_true,y_pred)
  mse=tf.keras.metrics.MeanSquaredError()
  mse.update_state(y_true,y_pred)
  rmse=tf.keras.metrics.RootMeanSquaredError()
  rmse.update_state(y_true,y_pred)
  mape=tf.keras.metrics.MeanAbsolutePercentageError()
  mape.update_state(y_true,y_pred)

  return {"mae":mae.result().numpy(),"mse":mse.result().numpy(),"rmse":rmse.result().numpy(),"mape":mape.result().numpy(),"mase":mase(y_true,y_pred).numpy()}

naive_results=metric(y_test[1:],naive_forecast)
naive_results