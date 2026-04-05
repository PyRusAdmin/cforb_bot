import os

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
USER_PROXY = os.getenv("PROXY_USER")
PASSWORD_PROXY = os.getenv("PROXY_PASSWORD")
IP_PROXY = os.getenv("PROXY_IP")
PORT_PROXY = os.getenv("PROXY_PORT")

storage = MemoryStorage()  # Создаем хранилище
dp = Dispatcher(storage=storage)  # Создаём диспетчер

# Используем SOCKS5 прокси через URL
session = AiohttpSession(proxy=f"socks5://{USER_PROXY}:{PASSWORD_PROXY}@{IP_PROXY}:{PORT_PROXY}")

bot = Bot(
    token=BOT_TOKEN,  # Токен бота
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),  # Устанавливаем parse_mode для HTML
    session=session,  # Устанавливаем сессию для бота и прокси
)

ADMIN_USER_ID = 535185511, 301634256

router = Router()
dp.include_router(router)
