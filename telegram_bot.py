import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise RuntimeError("Telegram environment variables missing")

bot = Bot(token=TOKEN)

async def send_signal(symbol, side, entry, tp, sl):
    message = f"""
🚨 *{side} SIGNAL*
🪙 {symbol}

📍 Entry: {entry:.4f}
🎯 TP: {tp:.4f}
🛑 SL: {sl:.4f}

RR: 1:2.5
TF: 5M
"""
    await bot.send_message(
        chat_id=CHAT_ID,
        text=message,
        parse_mode="Markdown"
    )
