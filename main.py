import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Insert your bot's token here
API_TOKEN = '6869009013:AAHrXXdTY20bwnLo4S9jx0xZaRHx3qv_HQs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Handler for the start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nSend me any message and I'll echo it back!")

# Handler for the help command
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Send me any message and I'll echo it back!")

# Handler for all other messages
@dp.message_handler()
async def echo(message: types.Message):
    # Echo the received message
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
