import yfinance as yf
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

#Create Dataframe -> Later optimize for user input
class MovingAverages():
    global tickerSymbol
    global tickerData
    global timeframe
    tickerSymbol = yf.Ticker('AAPL')#Identifies which stock to look at --> in this case Apple
    tickerData = tickerSymbol.history(period = '1y', interval = '1d', start = '2020-3-1', end = '2020-5-24')#Paramters for data of stock(constructs data frame)

    timeframe = int(input("How many days is your moving average: "))

    def ExponentialMovingAverage(timeframe):
        ema = tickerData['Close'].ewm(span = timeframe, adjust = False).mean()
        ema.plot(grid = True)
        print(ema)

    def SimpleMovingAverage(timeframe):
        tickerData['Close'].plot()
        print(tickerData['Close'].rolling(window = timeframe).mean())
        plt.show()

    ExponentialMovingAverage(timeframe) #Test for EMA Method
    SimpleMovingAverage(timeframe) #Test for SMA Method
