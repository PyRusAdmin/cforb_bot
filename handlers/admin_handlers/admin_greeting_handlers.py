import os
import sqlite3

import openpyxl
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from loguru import logger

from database.database import recording_data_of_users_who_launched_the_bot
from keyboards.admin_keyboards.admin_keyboards import admin_create_greeting_keyboard
from system.dispatcher import bot, dp


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


def create_excel_file_start(orders):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    # Заголовки столбцов
    sheet['A1'] = 'user_id'
    sheet['B1'] = 'username'
    sheet['C1'] = 'first_name'
    sheet['D1'] = 'last_name'
    sheet['E1'] = 'join_date'
    # Заполнение данными заказов
    for index, order in enumerate(orders, start=2):
        sheet.cell(row=index, column=1).value = order[0]  # user_id
        sheet.cell(row=index, column=2).value = order[1]  # username
        sheet.cell(row=index, column=3).value = order[2]  # first_name
        sheet.cell(row=index, column=4).value = order[3]  # last_name
        sheet.cell(row=index, column=5).value = order[4]  # join_date

    return workbook


@dp.callback_query_handler(lambda c: c.data == 'get_users_who_launched_the_bot')
async def get_users_who_launched_the_bot(message: types.Message):
    try:
        if message.from_user.id not in [535185511]:
            await message.reply('У вас нет доступа к этой команде.')
            return
        # Подключение к базе данных SQLite
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        # Получение данных из базы данных
        cursor.execute("SELECT * FROM users_start")
        orders = cursor.fetchall()
        # Создание файла Excel
        workbook = create_excel_file_start(orders)
        filename = 'Данные пользователей запустивших бота.xlsx'
        workbook.save(filename)  # Сохранение файла
        with open(filename, 'rb') as file:
            text = ("Данные пользователей запустивших бота\n\n"
                    "Для запуска админ панели или возврата в начальное меню нажми на /start_admin")
            await bot.send_document(message.from_user.id, document=file, caption=text)  # Отправка файла пользователю
        os.remove(filename)  # Удаление файла
    except Exception as e:
        logger.error(e)


def register_admin_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(admin_send_start)  # Обработчик команды /start, он же пост приветствия 👋
    dp.register_message_handler(export_data)  # Обработчик команды /start, он же пост приветствия 👋
    dp.register_message_handler(get_users_who_launched_the_bot)  # Обработчик команды /start, он же пост приветствия 👋
