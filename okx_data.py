import requests
import pandas as pd

BASE_URL = "https://www.okx.com"

def fetch_ohlcv(symbol, timeframe="5m", limit=200):
    url = f"{BASE_URL}/api/v5/market/candles"
    params = {
        "instId": symbol,
        "bar": timeframe,
        "limit": limit
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()

        if data["code"] != "0":
            return None

        rows = data["data"]
        rows.reverse()

        df = pd.DataFrame(rows, columns=[
            "time","open","high","low","close",
            "volume","volumeCcy","volumeCcyQuote","confirm"
        ])

        df = df[["time","open","high","low","close","volume"]].astype(float)
        return df

    except Exception as e:
        print(f"[FETCH ERROR] {symbol}: {e}")
        return None
