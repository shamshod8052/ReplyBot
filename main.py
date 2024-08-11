from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from environs import Env

# Get env variables
env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
TEXT = env.str('TEXT')
ADMIN_CHAT_ID = env.int('ADMIN_CHAT_ID')

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Get Message type updates
@dp.message_handler()
async def answer_for_message(message: types.Message):
    await message.reply(TEXT)

# Get CallbackQuery type updates
@dp.callback_query_handler()
async def answer_for_callback(call: types.CallbackQuery):
    await call.answer()
    await call.message.reply(TEXT)

async def on_startup(dp):
    # A message will be sent when the bot starts
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text="🤖 The bot has started 🚀")

async def on_shutdown(dp):
    # A message is sent when the bot is stopped
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text="🤖 The bot has been stopped 🛑")

if __name__ == '__main__':
    print("Started...")
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=False)
