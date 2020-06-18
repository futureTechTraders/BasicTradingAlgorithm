
import yfinance as yf
import pandas as pd
import matplotlib as mpl  
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go

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



#CODE TO PLOT THE DATAFRAME STARTS HERE
#necessary import statements above
mpf.plot(
            tickerData,
            type='candle',
            style = 'charles',
            title = str(userTicker) + " stock",
            ylabel='Price ($)',
            volume = True,
            ylabel_lower = 'volume',
            show_nontrading = True
        )

'''
candlestick = go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close']
                            )

fig = go.Figure(data=[candlestick])

fig.update_layout(
    width=800, height=600,
    title= str(userTicker) + " stock",
    yaxis_title= str(userTicker) + ' price',
)

fig.show()




'''
