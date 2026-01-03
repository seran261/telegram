from config import EMA_LENGTH, LIQ_LOOKBACK, RR_RATIO

def ema(series, length):
    return series.ewm(span=length).mean()

def check_signal(df):
    if df is None or len(df) < 60:
        return None

    df["ema"] = ema(df["close"], EMA_LENGTH)
    last = df.iloc[-1]

    liq_high = df["high"].rolling(LIQ_LOOKBACK).max().iloc[-2]
    liq_low  = df["low"].rolling(LIQ_LOOKBACK).min().iloc[-2]

    # BUY
    if last["low"] < liq_low and last["close"] > last["ema"] and last["close"] > last["open"]:
        entry = last["close"]
        sl = liq_low
        tp3 = entry + (entry - sl) * RR_RATIO
        tp1 = entry + (tp3 - entry) * 0.3
        tp2 = entry + (tp3 - entry) * 0.6
        return ("BUY", entry, sl, [tp1, tp2, tp3])

    # SELL
    if last["high"] > liq_high and last["close"] < last["ema"] and last["close"] < last["open"]:
        entry = last["close"]
        sl = liq_high
        tp3 = entry - (sl - entry) * RR_RATIO
        tp1 = entry - (entry - tp3) * 0.3
        tp2 = entry - (entry - tp3) * 0.6
        return ("SELL", entry, sl, [tp1, tp2, tp3])

    return None
