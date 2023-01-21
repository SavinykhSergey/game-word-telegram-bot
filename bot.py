from aiogram import Bot, Dispatcher
from config import TOKEN
import logging

def create_bot():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)
    return bot, dp