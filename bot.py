import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8731409801:AAGdv7egd443UFVAfNom2lu6Ll815huTXpY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! 👋")


@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())