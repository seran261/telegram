import asyncio
from binance_data import fetch_ohlcv
from strategy import check_signal
from telegram_bot import send_signal

TOP_COINS = [...]

async def run():
    while True:
        for symbol in TOP_COINS:
            df = fetch_ohlcv(symbol)
            signal = check_signal(df)
            if signal:
                side, entry, tp, sl = signal
                await send_signal(symbol, side, entry, tp, sl)
                await asyncio.sleep(10)
        await asyncio.sleep(60)

asyncio.run(run())
