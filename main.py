import asyncio
from okx_data import fetch_ohlcv
from strategy import check_signal
from trade_manager import register_trade, check_trade
from telegram_bot import send_signal, send_hit
from config import SYMBOLS, TIMEFRAME, SCAN_DELAY

async def run():
    print("🚀 OKX Bot Running")

    while True:
        for s in SYMBOLS:
            df = fetch_ohlcv(s, TIMEFRAME)
            if df is None: 
                continue

            price = df.iloc[-1]["close"]

            r = check_trade(s, price)
            if r:
                await send_hit(s, r)

            sig = check_signal(df)
            if sig:
                side, entry, sl, tps = sig
                register_trade(s, side, sl, tps)
                await send_signal(s, side, entry, sl, tps)
                await asyncio.sleep(5)

        await asyncio.sleep(SCAN_DELAY)

asyncio.run(run())
