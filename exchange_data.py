import ccxt
import pandas as pd

exchange = ccxt.bybit({
    "enableRateLimit": True,
    "options": {
        "defaultType": "linear",      # ✅ FORCE USDT PERPETUAL
        "fetchMarkets": "linear"      # ✅ DO NOT TOUCH SPOT
    }
})

# 🔒 Load markets ONCE (important)
exchange.load_markets()

def fetch_ohlcv(symbol, timeframe="5m", limit=200):
    try:
        data = exchange.fetch_ohlcv(
            symbol,
            timeframe=timeframe,
            limit=limit,
            params={"category": "linear"}  # ✅ FORCE LINEAR
        )
        return pd.DataFrame(
            data,
            columns=["time","open","high","low","close","volume"]
        )
    except Exception as e:
        print(f"[FETCH ERROR] {symbol}: {e}")
        return None
