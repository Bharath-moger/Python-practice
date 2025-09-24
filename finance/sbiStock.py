import yfinance as yf

# ticker for State Bank of India on Yahoo (NSE)
t = yf.Ticker("GTL.NS")

# quick info
info = t.info
print("Current price:", info.get("regularMarketPrice"))
print("Previous close:", info.get("previousClose"))

# historical data (last 7 days, daily)
hist = t.history(period="7d", interval="1d")
print(hist)            # DataFrame with Open/High/Low/Close/Volume

# intraday (if available): 1d with 1m interval
intraday = t.history(period="1d", interval="1h")
print(intraday.tail())
