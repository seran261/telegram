import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise RuntimeError("Telegram env variables missing")

bot = Bot(token=TOKEN)

async def send_signal(symbol, side, entry, sl, tps):
    msg = f"""
🚨 *{side} SIGNAL*
🪙 {symbol}

Entry: {entry:.4f}
SL: {sl:.4f}
TP1: {tps[0]:.4f} (30%)
TP2: {tps[1]:.4f} (30%)
TP3: {tps[2]:.4f} (40%)
"""
    await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")

async def send_hit(symbol, result):
    await bot.send_message(
        chat_id=CHAT_ID,
        text=f"📌 *{symbol}* → `{result} HIT`",
        parse_mode="Markdown"
    )
