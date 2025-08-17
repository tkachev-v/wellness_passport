import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from app.handlers import router

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())








