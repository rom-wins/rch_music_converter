from aiogram import types
from aiogram.filters.command import CommandObject

EMPTY_USERNAME_ERROR_MESSAGE = "Error: Empty username."
EMPTY_TOKEN_ERROR_MESSAGE = "Error: No token found."
EMPTY_CONVERT_URL_ERROR_MESSAGE = "Error: No url found."

class Validator:
    @staticmethod
    def validate_message(message: types.Message):
        if message.from_user.username is None:
            raise RuntimeError(EMPTY_USERNAME_ERROR_MESSAGE)

    @staticmethod
    def validate_add_token_command(command: CommandObject):
        if command.args is None:
            raise RuntimeError(EMPTY_TOKEN_ERROR_MESSAGE)

    @staticmethod
    def validate_convert_command(command: CommandObject):
        if command.args is None:
            raise RuntimeError(EMPTY_CONVERT_URL_ERROR_MESSAGE)