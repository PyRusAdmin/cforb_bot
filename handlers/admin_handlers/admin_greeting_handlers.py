from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from loguru import logger

from database.database import check_user_exists_in_db
from database.database import recording_data_of_users_who_launched_the_bot
from keyboards.admin_keyboards.admin_keyboards import admin_create_greeting_keyboard
from keyboards.user_keyboards.user_keyboards import create_greeting_keyboard
from keyboards.user_keyboards.user_keyboards import create_my_details_keyboard
from system.dispatcher import bot, dp
import openpyxl
import os
import sqlite3


@dp.message_handler(commands=['admin_start'])
async def admin_send_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию

    # Получаем информацию о пользователе
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    join_date = message.date.strftime("%Y-%m-%d %H:%M:%S")

    logger.info(f"Пользователь {username} ({user_id}) запустил бота в {join_date}")
    # Записываем информацию о пользователе в базу данных
    recording_data_of_users_who_launched_the_bot(user_id, username, first_name, last_name, join_date)

    greeting_keyboard = admin_create_greeting_keyboard()
    data = (f"<b>Привет админ {first_name} {last_name}, спасибо что поддерживаешь на нашего бота 🤖!</b>\n\n"
            f"Для запуска админ панели нажми на /start_admin")
    await bot.send_message(message.from_user.id, text=data, reply_markup=greeting_keyboard, parse_mode=ParseMode.HTML)


# Функция для создания файла Excel с данными заказов
def create_excel_file(orders):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    # Заголовки столбцов
    sheet['A1'] = 'ID аккаунта пользователя'
    sheet['B1'] = 'Имя'
    sheet['C1'] = 'Фамилия'
    sheet['D1'] = 'Город'
    sheet['E1'] = 'Номер телефона'
    sheet['F1'] = 'Дата регистрации'
    # Заполнение данными заказов
    for index, order in enumerate(orders, start=2):
        sheet.cell(row=index, column=1).value = order[0]  # ID аккаунта пользователя
        sheet.cell(row=index, column=2).value = order[1]  # Имя
        sheet.cell(row=index, column=3).value = order[2]  # Фамилия
        sheet.cell(row=index, column=4).value = order[3]  # Город
        sheet.cell(row=index, column=5).value = order[4]  # Номер телефона
        sheet.cell(row=index, column=6).value = order[5]  # Дата регистрации

    return workbook


# Обработчик команды для выгрузки данных в Excel
@dp.callback_query_handler(lambda c: c.data == 'get_a_list_of_users_registered_in_the_bot')
async def export_data(message: types.Message):
    try:
        if message.from_user.id not in [535185511]:
            await message.reply('У вас нет доступа к этой команде.')
            return
        # Подключение к базе данных SQLite
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        # Получение данных из базы данных
        cursor.execute("SELECT * FROM users")
        orders = cursor.fetchall()
        # Создание файла Excel
        workbook = create_excel_file(orders)
        filename = 'Зарегистрированные пользователи в боте.xlsx'
        workbook.save(filename)  # Сохранение файла
        with open(filename, 'rb') as file:
            text = ("Данные пользователей зарегистрированных в боте\n\n"
                    "Для запуска админ панели или возврата в начальное меню нажми на /start_admin")
            await bot.send_document(message.from_user.id, document=file, caption=text)  # Отправка файла пользователю
        os.remove(filename)  # Удаление файла
    except Exception as e:
        logger.error(e)


@dp.callback_query_handler(lambda c: c.data == "admin_main_menu")
async def send_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию

        # Получаем информацию о пользователе
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name

        logger.info(f"Пользователь {username} ({user_id}) вернулся в начальное меню")

        user_exists = check_user_exists_in_db(user_id)  # Проверяем наличие пользователя в базе данных
        if user_exists:
            greeting_keyboard = create_greeting_keyboard()
            with open("media/photos/greeting.jpg", "rb") as photo_file:  # Загружаем фото для поста
                data = (f"<b>{first_name} {last_name}, спасибо что подписались на нашего бота!</b>\n\n"
                        "<b>🇨🇳 Компания CFB - предлагает широкий спектр услуг по бизнесу с Китаем!</b>\n\n"
                        "• С полным списком услуг Вы можете ознакомиться в меню бота.\n\n"
                        "Обязательно включите уведомления и не удаляйте этого бота из своих чатов!\n\n"
                        "• У Вас появится возможность мгновенно и автоматически получать актуальные прайс-листы, "
                        "необходимую информацию по обновлениям и т.д.\n\n"
                        "<i>Сайт: www.cforb.ru</i>\n"
                        "<i>Telegram: https://t.me/cforb_tg</i>\n"
                        "<i>Вконтакте: https://vk.com/cforb</i>\n"
                        "<i>Instagram: https://www.instagram.com/cforb_in</i>\n"
                        "<i>YouTube: https://www.youtube.com/@cforb_tube</i>")
                await bot.send_photo(message.from_user.id, caption=data, photo=photo_file,
                                     reply_markup=greeting_keyboard, parse_mode=ParseMode.HTML)
        else:
            # Если пользователя нет в базе данных, предлагаем пройти регистрацию
            sign_up_text = ("⚠️ <b>Вы не зарегистрированы в нашей системе</b> ⚠️\n\n"
                            "Для доступа к этому разделу, пожалуйста, <b>зарегистрируйтесь</b>.\n\n"
                            "Для перехода в начальное меню нажмите /start")

            # Создаем клавиатуру с помощью my_details() (предполагается, что она существует)
            my_details_key = create_my_details_keyboard()
            # Отправляем сообщение с предложением зарегистрироваться и клавиатурой
            await bot.send_message(message.from_user.id, sign_up_text,
                                   reply_markup=my_details_key,
                                   parse_mode=ParseMode.HTML,
                                   disable_web_page_preview=True)
    except Exception as error:
        logger.exception(error)


def register_admin_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(admin_send_start)  # Обработчик команды /start, он же пост приветствия 👋
    dp.register_message_handler(export_data)  # Обработчик команды /start, он же пост приветствия 👋
