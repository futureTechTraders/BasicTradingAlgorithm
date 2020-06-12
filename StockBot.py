import yfinance as yf
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

global tickerData
global timeFrame

class TickerDataFrame:
    def __init__(self,tSymbol,period, interval, start, end):
        self.tickerSymbol = tSymbol
        self.period = period
        self.interval = interval
        self.start = start
        self.end = end
        
    def createDataFrame(self):
        symbol = yf.Ticker(self.tickerSymbol)
        tickerData = symbol.history(period = self.period, interval = self.interval, start = self.start, end = self.end)#Edit these parameters for user input later
        return tickerData

#Below are the 'messages' that should appear in the app, for each respective element
userTicker = input('Please enter your selected stocks ticker: ')
period = input('please enter period(EX: 1Y, 9M, 1W, 20D): ')
interval = input('please enter interval(EX: 1D): ')
start = input('please enter start date in year/month/day(EX: 2019-3-1): ')
end = input('please enter end date in year/month/day(EX: 2020-5-1 ): ')
timeframe = int(input("How many days is your moving average: "))


symbol = TickerDataFrame(userTicker, period, interval, start, end)
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

class macd(MovingAverages):
    def __init__(self,tickerDataNew):
        self.tickerDataNew = tickerDataNew
       
    def calculateMACD(self):
        self.tickerDataNew.to_csv('MACD_Manipulation.txt')
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

        return df


class executeStockBot(macd):
    
    def __init__(self,timeframe,tickerDataNew):
        MovingAverages.__init__(self,timeframe)
        macd.__init__(self,tickerDataNew)
   
    def calculateEntryPoint(self):
        userStock = MovingAverages(self.timeframe)
        macdNew = macd(self.tickerDataNew)
        df = macdNew.calculateMACD()
        userStock.SimpleMovingAverage()
        lastClosePrice = tickerData['Close'].iloc[((tickerData['Close'].count()) - 1)]
        nullValues = tickerData['SMA'].isnull().sum(axis = 0)
        smaLastPrice = tickerData['SMA'].iloc[(((tickerData['SMA'].count()) + nullValues) - 1)]
    

        lastSignalPrice = df['signal'].iloc[((df['signal'].count()) - 1)]
        lastMACDPrice = df['MACD'].iloc[((df['MACD'].count()) - 1)]


        if((lastClosePrice > smaLastPrice) and ((lastMACDPrice > lastSignalPrice) or (lastMACDPrice > 0))):
            print('Enter a long position at ' + str(lastClosePrice))
        elif ((lastClosePrice  < smaLastPrice) and ((lastMACDPrice < lastSignalPrice) or (lastMACDPrice < 0))):
            print('Enter a short position at ' + str(lastClosePrice))
        else:
            print('No position should be taken, as there is no MACD & SMA agreement/consensus')


entryPoints = executeStockBot(timeframe,tickerData)
entryPoints.calculateEntryPoint()


    
