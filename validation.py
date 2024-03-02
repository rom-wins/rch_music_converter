from aiogram import types

EMPTY_USERNAME_ERROR_MESSAGE = "Error: Empty username."

class Validator:
    @staticmethod
    def validate_message(message: types.Message):
        if message.from_user.username is None:
            raise RuntimeError(EMPTY_USERNAME_ERROR_MESSAGE)