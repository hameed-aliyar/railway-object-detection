import asyncio
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import FSInputFile
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_IDS

bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def send_telegram_notification(message, image_path=None):
    try:
        for chat_id in TELEGRAM_CHAT_IDS:
            if image_path:
                photo = FSInputFile(image_path)
                await bot.send_photo(chat_id=chat_id, photo=photo, caption=message)
            else:
                await bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Telegram error: {str(e)}")
