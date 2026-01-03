from config import EMA_LENGTH, LIQ_LOOKBACK, RR_RATIO

def ema(series, length):
    return series.ewm(span=length).mean()

def check_signal(df):
    # =====================
    # SAFETY CHECK
    # =====================
    if df is None or len(df) < 80:
        return None

    # =====================
    # INDICATORS
    # =====================
    df["ema"] = ema(df["close"], EMA_LENGTH)
    df["vol_avg"] = df["volume"].rolling(20).mean()

    last = df.iloc[-1]
    prev = df.iloc[-2]

    # =====================
    # STRUCTURE LEVELS
    # =====================
    recent_high = df["high"].rolling(LIQ_LOOKBACK).max().iloc[-3]
    recent_low  = df["low"].rolling(LIQ_LOOKBACK).min().iloc[-3]

    # =====================
    # VOLUME SPIKE (RELAXED)
    # =====================
    volume_spike = last["volume"] > last["vol_avg"] * 1.2

    # =====================
    # 🟢 BUY — BREAK & RETEST (ZONE BASED)
    # =====================
    breakout_up = prev["close"] > recent_high
    retest_up = (
        last["low"] <= recent_high * 1.003 and   # zone retest
        last["close"] > recent_high
    )

    if (
        breakout_up and
        retest_up and
        last["close"] > df["ema"].iloc[-5] and   # trend bias
        last["close"] > last["open"] and
        volume_spike
    ):
        entry = last["close"]

        # SL: SCALP tight | SWING wide
        sl = recent_high * (0.998 if EMA_LENGTH <= 50 else 0.995)

        tp3 = entry + (entry - sl) * RR_RATIO
        tp1 = entry + (tp3 - entry) * 0.3
        tp2 = entry + (tp3 - entry) * 0.6

        return ("BUY", entry, sl, [tp1, tp2, tp3])

    # =====================
    # 🔴 SELL — BREAK & RETEST (ZONE BASED)
    # =====================
    breakout_down = prev["close"] < recent_low
    retest_down = (
        last["high"] >= recent_low * 0.997 and
        last["close"] < recent_low
    )

    if (
        breakout_down and
        retest_down and
        last["close"] < df["ema"].iloc[-5] and
        last["close"] < last["open"] and
        volume_spike
    ):
        entry = last["close"]

        # SL: SCALP tight | SWING wide
        sl = recent_low * (1.002 if EMA_LENGTH <= 50 else 1.005)

        tp3 = entry - (sl - entry) * RR_RATIO
        tp1 = entry - (entry - tp3) * 0.3
        tp2 = entry - (entry - tp3) * 0.6

        return ("SELL", entry, sl, [tp1, tp2, tp3])

    return None
