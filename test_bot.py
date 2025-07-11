import asyncio
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import FSInputFile

TELEGRAM_BOT_TOKEN = "7889811135:AAGiJbLpbtGhM1w1kKWEhTkmZbW0bUeylUo"
TELEGRAM_CHAT_IDS = ["7314060816"]

bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def send_test_message():
    for chat_id in TELEGRAM_CHAT_IDS:
        await bot.send_message(chat_id=chat_id, text="✅ Test message from Railway Bot!")

asyncio.run(send_test_message())
