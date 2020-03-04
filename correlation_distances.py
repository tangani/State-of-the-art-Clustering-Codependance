import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
import scipy

tickers = yf.Tickers('msft aapl goog tsla pypl amzn ebay toms, dmlry ttmi tmm ttm')
prices = tickers.download('max')['Close'] 

log_rets = np.log(prices).diff().dropna()
corr = log_rets.corr()
distance = np.sqrt(2*(1-corr))
sns.heatmap(distance, cmap=sns.color_palette("BuGn", 1000))

condenced_distance = scipy.spatial.distance.squareform(distance)