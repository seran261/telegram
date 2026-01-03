import ccxt
import pandas as pd

exchange = ccxt.binance({
    "enableRateLimit": True,
    "options": {"defaultType": "future"}
})

def fetch_ohlcv(symbol, timeframe="5m", limit=150):
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(
        data, columns=["time","open","high","low","close","volume"]
    )
    return df
