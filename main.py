from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.client.session.aiohttp import AiohttpSession
from config_reader import config
from models import Data
from service import ConvertService
from validation import Validator
from typing import Optional
import asyncio
import logging


logging.basicConfig(level=logging.INFO)

proxy_url = config.proxy_server.get_secret_value()
session = None
if proxy_url != "no_proxy":
    session = AiohttpSession(proxy=proxy_url)

bot = Bot(token=config.bot_token.get_secret_value(), session=session)
dp = Dispatcher()
data = Data()
convert_service = ConvertService()

def parse_yandex_token(command: CommandObject) -> Optional[str]:
    try:
        Validator.validate_add_token_command(command)
        return command.args.split(" ", maxsplit=1)[0]
    except ValueError:
        raise RuntimeError(
            "Error: wrong command format. Example:\n"
            f"/{command.command} <token>"
        )

def parse_convert_url(command: CommandObject) -> Optional[str]:
    try:
        Validator.validate_convert_command(command)
        return command.args.split(" ", maxsplit=1)[0]
    except ValueError:
        RuntimeError(
            "Error: wrong command format. Example:\n"
            f"/{command.command} <url>"
        )

@dp.message(Command("convert_youtube_to_yandex"))
async def cmd_convert_youtube_to_yandex(message: types.Message, command: CommandObject) -> None:
    try:
        Validator.validate_message(message)
        yandex_token = data.get_yandex_token(message.from_user.username)
        yt_music_url = parse_convert_url(command)
        convert_service.convert_youtube_to_yandex(yt_music_url, yandex_token)
    except Exception as ex:
        await message.answer(str(ex))
        return

    await message.answer("Playlist conversion from youtube to yandex successfully!")

@dp.message(Command("add_yandex_token"))
async def cmd_add_yandex_token(message: types.Message, command: CommandObject) -> None:
    try:
        Validator.validate_message(message)
        yandex_token = parse_yandex_token(command)
        data.save_yandex_token(message.from_user.username, yandex_token)
    except Exception as ex:
        await message.answer(str(ex))
        return

    await message.answer("Yandex token added successfully!\n")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        Validator.validate_message(message)
        data.create_user(message.from_user.username)
    except Exception as ex:
        await message.answer(str(ex))
        return

    await message.answer("Register success!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
