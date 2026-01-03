from telegram import Bot
import os

bot = Bot(token=os.getenv("8165069362:AAFr0v5wFlAvtKFgH-qDU1GFTlmh8OZWX78"))
CHAT_ID = os.getenv("7951298168")

async def send_signal(symbol, side, entry, tp, sl):
    msg = f"""
🚨 *{side} SIGNAL* 🚨
🪙 {symbol}

📍 Entry: `{entry:.4f}`
🎯 TP: `{tp:.4f}`
🛑 SL: `{sl:.4f}`

📊 RR: 1:2.5
⏱ TF: 5M
"""
    await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")
