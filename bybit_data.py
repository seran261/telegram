import requests
import pandas as pd

BASE_URL = "https://api.bybit.com"

def fetch_ohlcv(symbol, interval="5", limit=200):
    url = f"{BASE_URL}/v5/market/kline"
    params = {
        "category": "linear",
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()

        if data["retCode"] != 0:
            return None

        rows = data["result"]["list"]
        rows.reverse()  # oldest → newest

        df = pd.DataFrame(rows, columns=[
            "time","open","high","low","close","volume","turnover"
        ])

        df = df[["time","open","high","low","close","volume"]].astype(float)
        return df

    except Exception as e:
        print(f"[FETCH ERROR] {symbol}: {e}")
        return None
