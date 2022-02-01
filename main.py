import ccxt, yfinance
import pandas_ta as ta
import pandas as pd
from discord_webhook import DiscordWebhook

discordServer = "https://discord.com/api/webhooks/937803015505719296/j8SlyhlhePiGZ4EZdYgPKmtRwRel991lNxjvWhDxb1_mGw2lOUGDeJuHQ9O0fKLFDWb9"

ticker = "ETH/USDT"
timeframe = "5m"
periods = 500

exchange = ccxt.binance()

bars = exchange.fetch_ohlcv(ticker, timeframe=timeframe, limit = periods)

df = pd.DataFrame(bars, columns=["time", "open","high","low","close","volume"])

rsi = df.ta.rsi()
ema = df.ta.ema()
macd = df.ta.macd()

df = pd.concat([df, rsi,ema, macd], axis = 1)
last_row = df.iloc[-1]

text = "test"
DiscordWebhook(url=discordServer, content=text).execute()

print(last_row)

