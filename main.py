import asyncio
from exchange_data import fetch_ohlcv
from strategy import check_signal
from telegram_bot import send_signal
from config import SYMBOLS, TIMEFRAME, SCAN_DELAY

async def run():
    print("🚀 Bot started")

    while True:
        for symbol in SYMBOLS:
            df = fetch_ohlcv(symbol, TIMEFRAME)

            if df is None or df.empty:
                continue

            signal = check_signal(df)
            if signal:
                side, entry, tp, sl = signal
                await send_signal(symbol, side, entry, tp, sl)
                await asyncio.sleep(10)

        await asyncio.sleep(SCAN_DELAY)

asyncio.run(run())
