import yfinance as yf
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

global tickerData
class TickerDataFrame:
    def __init__(self,tSymbol):
        self.tickerSymbol = tSymbol
       
    def createDataFrame(self):
        symbol = yf.Ticker(self.tickerSymbol)
        tickerData = symbol.history(period = '1y', interval = '1d', start = '2020-3-1', end = '2020-5-30')#Edit these parameters for user input later
        return tickerData

symbol = input('Enter a stock ticker symbol')
tickerSymbol = TickerDataFrame(symbol)
tickerData = tickerSymbol.createDataFrame()

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

class MACD(MovingAverages):
    tickerData.to_csv('MACD_Manipulation.txt')
    df = pd.read_csv('MACD_Manipulation.txt', index_col = 'Date', parse_dates= True)
    fastperiod = MovingAverages(12)
    slowperiod = MovingAverages(26)
    df['12EMA'] = fastperiod.ExponentialMovingAverage() 
    df['26EMA'] = slowperiod.ExponentialMovingAverage()
    #create an array then convert to column in dataframe
    df['MACD'] = fastperiod.ExponentialMovingAverage() #PlaceHolder values 
    df['Axis'] = fastperiod.ExponentialMovingAverage() #PlaceHolder values
    for x in range(0,((df['26EMA'].count()))):
        macdCalc = (df['12EMA'].iloc[x]) - (df['26EMA'].iloc[x])
        df['MACD'].iloc[x] = macdCalc
        x += 1
        
    for x in range (0,df['MACD'].count()):
        df['Axis'].iloc[x] = 0


    df['signal'] = df['MACD'].ewm(span = 9, adjust = False).mean()

    plt.plot(df['MACD'])
    #plt.plot(df['signal'])
    #plt.plot(df['Axis'])
    plt.show()
    

    #Code to plot the closing prices, and MACD with signal line --> two seperate plots
    
    


   
