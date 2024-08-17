from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from environs import Env

env = Env()
env.read_env()

BOT_USERNAME = env.str('BOT_USERNAME')

class MessageFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        result = False
        if message.chat.type == 'private' or BOT_USERNAME in message.text:
            result = True
        return result


class CallbackFilter(BoundFilter):
    async def check(self, call: types.CallbackQuery) -> bool:
        result = False
        if call.message.chat.type == 'private':
            result = True
        return result
