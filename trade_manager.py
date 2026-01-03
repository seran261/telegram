active_trades = {}

def register_trade(symbol, side, entry, sl, tps):
    active_trades[symbol] = {
        "side": side,
        "entry": entry,
        "sl": sl,
        "tps": tps,
        "hit": [False, False, False]
    }

def check_trade(symbol, price):
    trade = active_trades.get(symbol)
    if not trade:
        return None

    side = trade["side"]

    # SL
    if (side == "BUY" and price <= trade["sl"]) or \
       (side == "SELL" and price >= trade["sl"]):
        del active_trades[symbol]
        return "SL"

    # TPs
    for i, tp in enumerate(trade["tps"]):
        if trade["hit"][i]:
            continue
        if (side == "BUY" and price >= tp) or \
           (side == "SELL" and price <= tp):
            trade["hit"][i] = True
            if i == 2:
                del active_trades[symbol]
            return f"TP{i+1}"

    return None
