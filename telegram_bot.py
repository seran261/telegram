import os
from telegram import Bot

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_signal(symbol, side, entry, sl, tps):
    await bot.send_message(
        chat_id=CHAT_ID,
        parse_mode="Markdown",
        text=f"""🚨 *{side} SIGNAL*
{symbol}

Entry: {entry:.4f}
SL: {sl:.4f}
TP1: {tps[0]:.4f}
TP2: {tps[1]:.4f}
TP3: {tps[2]:.4f}
"""
    )

async def send_hit(symbol, result):
    await bot.send_message(chat_id=CHAT_ID, text=f"{symbol} → {result} HIT")
