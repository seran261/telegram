import asyncio
from exchange_data import fetch_ohlcv
from strategy import check_signal
from trade_manager import register_trade, check_trade
from telegram_bot import send_signal, send_hit
from config import SYMBOLS, TIMEFRAME, SCAN_DELAY

async def run():
    print("🚀 Bybit Linear Bot Started")

    while True:
        for symbol in SYMBOLS:
            df = fetch_ohlcv(symbol, TIMEFRAME)
            if df is None or df.empty:
                continue

            price = df.iloc[-1]["close"]

            # Monitor TP / SL
            result = check_trade(symbol, price)
            if result:
                await send_hit(symbol, result)

            # New Signal
            signal = check_signal(df)
            if signal:
                side, entry, sl, tps = signal
                register_trade(symbol, side, entry, sl, tps)
                await send_signal(symbol, side, entry, sl, tps)
                await asyncio.sleep(10)

        await asyncio.sleep(SCAN_DELAY)

asyncio.run(run())
