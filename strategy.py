import pandas as pd
from config import EMA_LENGTH, LIQ_LOOKBACK, RR_RATIO

def ema(series, length):
    return series.ewm(span=length).mean()

def check_signal(df):
    if df is None or len(df) < 60:
        return None

    df["ema"] = ema(df["close"], EMA_LENGTH)

    last = df.iloc[-1]
    prev = df.iloc[-2]

    liq_high = df["high"].rolling(LIQ_LOOKBACK).max().iloc[-2]
    liq_low  = df["low"].rolling(LIQ_LOOKBACK).min().iloc[-2]

    # BUY CONDITIONS
    if (
        last["low"] < liq_low and
        last["close"] > last["ema"] and
        last["close"] > last["open"]
    ):
        entry = last["close"]
        sl = liq_low
        tp = entry + (entry - sl) * RR_RATIO
        return ("BUY", entry, tp, sl)

    # SELL CONDITIONS
    if (
        last["high"] > liq_high and
        last["close"] < last["ema"] and
        last["close"] < last["open"]
    ):
        entry = last["close"]
        sl = liq_high
        tp = entry - (sl - entry) * RR_RATIO
        return ("SELL", entry, tp, sl)

    return None
