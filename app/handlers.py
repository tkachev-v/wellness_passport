from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from app.pdf_handling import handle_pdf
from app.generate import responde
from prompt import prompt1, prompt2

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет! Я помощник для анализа паспорта благополучия, прикрепи PDF-файл, с который нужно проанализировать.')

@router.message(F.document)
async def generating(message: Message):
    response = await handle_pdf(message, prompt1)
    await message.answer(response)

@router.message()
async def responding(message: Message):
    response = await responde(message.text, prompt2)
    await message.answer(response)

