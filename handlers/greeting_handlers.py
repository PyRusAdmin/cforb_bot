import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram.types import ParseMode

from keyboards.user_keyboards import create_greeting_keyboard
from system.dispatcher import bot, dp


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    # Получаем информацию о пользователе
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    join_date = message.date.strftime("%Y-%m-%d %H:%M:%S")
    # Записываем информацию о пользователе в базу данных
    conn = sqlite3.connect("your_database.db")  # Замените "your_database.db" на имя вашей базы данных
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_start (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    join_date TEXT
                )''')
    cursor.execute("INSERT OR REPLACE INTO users_start (user_id, username, first_name, last_name, join_date) "
                   "VALUES (?, ?, ?, ?, ?)", (user_id, username, first_name, last_name, join_date))
    conn.commit()
    conn.close()

    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
    greeting_keyboard = create_greeting_keyboard()
    with open("media/photos/greeting.jpg", "rb") as photo_file:  # Загружаем фото для поста
        data = ("👤 Имя клиент, спасибо что подписались на нашего бота!\n\n"
                "🌐 Компания CFB - предлагает широкий спектр услуг по бизнесу с Китаем!\n"
                "📋 С полным списком услуг вы можете ознакомиться в меню бота.\n\n"
                "🔔 Обязательно подпишитесь, включите уведомления и не удаляйте этого бота из ваших чатов, и у Вас появится возможность мгновенно и автоматически получать актуальные прайс-листы, необходимую информацию и т.д.")
        await bot.send_photo(message.from_user.id, caption=data, photo=photo_file, reply_markup=greeting_keyboard, parse_mode=ParseMode.HTML)


def register_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(send_start)  # Обработчик команды /start, он же пост приветствия 👋
