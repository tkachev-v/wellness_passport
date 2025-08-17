from aiogram.types import Message
import os
from aiogram import Bot
import fitz
from dotenv import load_dotenv
from app.generate import analyzing
import shutil

load_dotenv()


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token= TELEGRAM_TOKEN)


def getting_text(file_path: str) -> str:
    text = ""

    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

async def handle_pdf(message:Message, prompt:str) -> str:

        file = await bot.get_file(message.document.file_id)
        file_path = file.file_path
        file_name = message.document.file_name
        local_path = os.path.join("pdf_files", file_name)
        os.makedirs("pdf_files", exist_ok=True)

        await bot.download_file(file_path, local_path)
        text = getting_text(local_path)
        os.remove(local_path)
        shutil.rmtree("pdf_files")
        summary = await analyzing(text,prompt)
        return summary