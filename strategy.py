import numpy as np

def ema(series, period=50):
    return series.ewm(span=period).mean()

def check_signal(df, rr=2.5, lookback=12):
    df["ema"] = ema(df["close"])
    df["vol_avg"] = df["volume"].rolling(20).mean()

    last = df.iloc[-1]
    prev = df.iloc[-2]

    liq_high = df["high"].rolling(lookback).max().iloc[-2]
    liq_low  = df["low"].rolling(lookback).min().iloc[-2]

    buy_sweep  = last["low"] < liq_low
    sell_sweep = last["high"] > liq_high

    volume_ok = last["volume"] > last["vol_avg"]

    if buy_sweep and last["close"] > last["ema"] and last["close"] > last["open"] and volume_ok:
        entry = last["close"]
        sl = liq_low
        tp = entry + (entry - sl) * rr
        return ("BUY", entry, tp, sl)

    if sell_sweep and last["close"] < last["ema"] and last["close"] < last["open"] and volume_ok:
        entry = last["close"]
        sl = liq_high
        tp = entry - (sl - entry) * rr
        return ("SELL", entry, tp, sl)

    return None
