import yfinance as yf
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

global tickerData
global timeFrame

class TickerDataFrame:
    def __init__(self,tSymbol):
        self.tickerSymbol = tSymbol
        
    def createDataFrame(self):
        symbol = yf.Ticker(self.tickerSymbol)
        tickerData = symbol.history(period = '1y', interval = '1d', start = '2020-3-1', end = '2020-3-27')#Edit these parameters for user input later
        return tickerData
userTicker = input('Please enter your selected stocks ticker: ')
symbol = TickerDataFrame(userTicker)
tickerData = symbol.createDataFrame()
class MovingAverages():
    def __init__(self,timeframe):
        self.timeframe = timeframe
    
    def ExponentialMovingAverage(self):
        tickerData['EMA'] = tickerData['Close'].ewm(span = self.timeframe, adjust = False).mean()
        return tickerData['EMA']
        #ema.plot(grid = True)
        #print(ema)

    def SimpleMovingAverage(self):
        #tickerData['Close'].plot()
        tickerData['SMA'] = tickerData['Close'].rolling(window = self.timeframe).mean()
        return tickerData['SMA']
        #plt.show()
    #ExponentialMovingAverage(timeframe) #Test for EMA Method
    #SimpleMovingAverage(timeframe) #Test for SMA Method
class executeStockBot(MovingAverages):
    timeframe = int(input("How many days is your moving average: "))
    userStock = MovingAverages(timeframe)
    userStock.SimpleMovingAverage()
    lastClosePrice = tickerData['Close'].iloc[((tickerData['Close'].count()) - 1)]
    nullValues = tickerData['SMA'].isnull().sum(axis = 0)
    smaLastPrice = tickerData['SMA'].iloc[(((tickerData['SMA'].count()) + nullValues) - 1)]
 
    if(lastClosePrice > smaLastPrice):
        print('Enter a long position at ' + str(lastClosePrice))
    elif (lastClosePrice  < smaLastPrice):
        print('Enter a short position at ' + str(lastClosePrice))
    else:
        print('No position should be taken')

    
    
