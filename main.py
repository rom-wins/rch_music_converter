import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.client.session.aiohttp import AiohttpSession
from config_reader import config

logging.basicConfig(level=logging.INFO)
session = AiohttpSession(proxy=config.proxy_server.get_secret_value())
bot = Bot(token=config.bot_token.get_secret_value(), session=session)
dp = Dispatcher()

USERS = {}
EMPTY_USERNAME_ERROR_MESSAGE = "Error: Empty username."

def save_user(username: str) -> None:
    if username in USERS.keys():
        return
    USERS[username] = {}

def validate_message(message: types.Message):
    if message.from_user.username is None:
        raise RuntimeError(EMPTY_USERNAME_ERROR_MESSAGE)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        validate_message(message)
        save_user(message.from_user.username)
    except Exception as ex:
        await message.answer(str(ex))
        return

    await message.answer("Register success!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())