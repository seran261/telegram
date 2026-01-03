import ccxt
import pandas as pd

exchange = ccxt.okx({
    "enableRateLimit": True,
    "options": {
        "defaultType": "swap"
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
        print(f"[FETCH ERROR] {symbol}: {e}")
        return None
