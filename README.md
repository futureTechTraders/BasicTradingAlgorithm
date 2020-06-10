# BasicTradingAlgorithm
Python trading algorithm which suggests entry and exit points based off SimpleMovingAverage, Relative Strength Index, and Moving Average Convergence Divergence

<h1> 
Data Collection
</h1>
Web scrapes yahoo finance to collect and store many price fields in a data frame. Price fields include open prices, close prices, volume, highs, lows, dividends, stock splits, adjusted close prices etc.

<h1>
Trading Methodology
</h1>

<h2>

Moving Averages

</h2>

If price level trends/crosses above a user-specified simple moving average, then enter position long as this would be a bullish indicator

If price level trends/crosses below a user-specified simple moving average, then enter position short as this would be a bearish indicator

<h2>
Moving Average Convergence Divergence(MACD)
</h2>
If MACD(12 day ema - 26 day ema) crosses below a 9-day exponential moving average(signal line), then enter position short as this would be a bearish indicator

If MACD(12 day ema - 26 day ema) crosses above a 9-day exponential moving average(signal line), then enter position long as this would be a bearish indicator  
