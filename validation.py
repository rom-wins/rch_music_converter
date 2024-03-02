from aiogram import types
from aiogram.filters.command import CommandObject

EMPTY_USERNAME_ERROR_MESSAGE = "Error: Empty username."
EMPTY_TOKEN_ERROR_MESSAGE = "Error: no token found."

class Validator:
    @staticmethod
    def validate_message(message: types.Message):
        if message.from_user.username is None:
            raise RuntimeError(EMPTY_USERNAME_ERROR_MESSAGE)

    @staticmethod
    def validate_add_token_command(command: CommandObject):
        if command.args is None:
            raise RuntimeError(EMPTY_TOKEN_ERROR_MESSAGE)
