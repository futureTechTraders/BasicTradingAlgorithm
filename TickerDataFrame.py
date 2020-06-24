import yfinance as yf
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
class TickerDataFrame:
    def __init__(self,tSymbol):
        self.tickerSymbol = tSymbol
        symbol = yf.Ticker(self.tickerSymbol)
    def createDataFrame(self):
        symbol = yf.Ticker(self.tickerSymbol)
        tickerData = symbol.history(period = '1d', start = date.today())
        #tickerData = symbol.history(period = '1y', interval = '1d', start = '2020-3-1', end = '2020-5-28')#Edit these parameters for user input later
        return tickerData


stockTicker = input("what stock would you like data for?: " )
df = TickerDataFrame(stockTicker)
pd.set_option('display.max_rows', None)
print(df.createDataFrame())

'''
YFinance Parameters:
Period: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max DEFAULT IS 1mo
Interval: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo DEFAULT IS 1d

















#tickerData.to_csv('stockData.csv')
#df = pd.read_csv('stockData.csv', header = 0, index_col = 'Dates', parse_dates = True)


#print(tickerData.loc[pd.Timestamp('2020-03-02'):pd.Timestamp('2020-03-25')])
#print(tickerData.loc[pd.Timestamp('2020-03-02'):pd.Timestamp('2020-03-25'), 'Open' : 'Close'])
#print(tickerData.iloc[0:6])
#print(tickerData.iloc[[0,2],[1,2]])
#print(tickerData.iloc[0:3, 1:2])


#print(tickerData.sample(2))

#print(tickerData.resample('M').mean())  -- resamples dataframe into monthly data, averaging the data

#tickerData['Diff'] = tickerData.Close - tickerData.Open #Adds a "difference" column to the DataFrame 


#tickerData['Close'] = np.log(tickerData['Close'] / tickerData['Close'].shift(1))




#pct_change = tickerData['Close'].pct_change()
#pct_change.fillna(0, inplace = True)

#print(pct_change)# prints close value as the % change from previous value

#print(np.log(pct_change + 1)) #Log returns: To get better insight of returns over time STUDY

#print(tickerData.resample('BM').apply(lambda x : x[-1]))



#pct_change.hist(bins = 50)
#plt.show()

#print(pct_change.describe()) #Describes the data in the Histogram: mean, standard deviation, percentile of points etc.




#print(tickerData.pct_change())


#print (tickerData.head())
                                    
