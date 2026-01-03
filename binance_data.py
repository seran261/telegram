import ccxt
import pandas as pd

exchange = ccxt.binanceusdm({
    "enableRateLimit": True,
    "options": {
        "defaultType": "future"
    }
})

def fetch_ohlcv(symbol, timeframe="5m", limit=200):
    try:
        data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        df = pd.DataFrame(
            data,
            columns=["time", "open", "high", "low", "close", "volume"]
        )
        return df
    except Exception as e:
        print(f"Fetch error {symbol}: {e}")
        return None
