import ccxt
import pandas as pd

exchange = ccxt.bybit({
    "enableRateLimit": True,
    "options": {
        "defaultType": "linear"  # USDT perpetual
    }
})

def fetch_ohlcv(symbol, timeframe="5m", limit=200):
    try:
        data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        return pd.DataFrame(
            data,
            columns=["time","open","high","low","close","volume"]
        )
    except Exception as e:
        print(f"[FETCH ERROR] {symbol}: {e}")
        return None
