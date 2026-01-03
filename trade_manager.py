active_trades = {}

def register_trade(symbol, side, sl, tps):
    active_trades[symbol] = {"side": side, "sl": sl, "tps": tps, "hit":[0,0,0]}

def check_trade(symbol, price):
    t = active_trades.get(symbol)
    if not t:
        return None

    if (t["side"]=="BUY" and price<=t["sl"]) or (t["side"]=="SELL" and price>=t["sl"]):
        del active_trades[symbol]
        return "SL"

    for i,tp in enumerate(t["tps"]):
        if not t["hit"][i]:
            if (t["side"]=="BUY" and price>=tp) or (t["side"]=="SELL" and price<=tp):
                t["hit"][i]=1
                if i==2: del active_trades[symbol]
                return f"TP{i+1}"
