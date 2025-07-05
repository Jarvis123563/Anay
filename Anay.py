from flask import Flask
from telegram import Bot
import asyncio
import threading
import time

# === Configuration ===
BOT_TOKEN = '7577331816:AAGiEqqsy-wynhxvVm8ZlTVU4I-2Mk_5RWQ'
MY_GROUP_ID = -1002501297731  # Replace with your group ID
SEND_INTERVAL = 200  # seconds

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)

@app.route('/health')
def health():
    return "Bot is alive ✅", 200

async def send_message():
    message_text = """
🚀 Join my channel for best loots and Complete 500 for giveaway

https://t.me/publicchannel8668
"""
    try:
        await bot.send_message(chat_id=MY_GROUP_ID, text=message_text)
        print("Message sent.")
    except Exception as e:
        print(f"Error sending message: {e}")

def run_async_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        loop.run_until_complete(send_message())
        time.sleep(SEND_INTERVAL)

if __name__ == '__main__':
    threading.Thread(target=run_async_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=8080)
  
