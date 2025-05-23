import os

from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(
    token=BOT_TOKEN,
)
storage = MemoryStorage()  # Хранилище
dp = Dispatcher(storage=storage)

ADMIN_USER_ID = 535185511, 301634256

router = Router()
dp.include_router(router)
