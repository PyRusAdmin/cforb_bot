import os
import sqlite3

import openpyxl
from aiogram import F
from aiogram import types
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile
from loguru import logger

from database.database import reading_from_database
from system.dispatcher import bot, ADMIN_USER_ID
from system.dispatcher import dp
from system.dispatcher import router


@router.message(Command('help'))
async def admin_send_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    await state.clear()  # Завершаем текущее состояние машины состояний
    """Админ панель"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Команды админа:\n\n"

                         "<b>Редактирование текста и отправка сообщений:</b>\n\n"
                         
                         "<b>Редактирование текста:</b>\n"
                         "✔️ /edit_types_of_packaging - Виды упаковки\n"
                         "✔️ /edit_services_and_prices - Услуги и цены\n"
                         "✔️ /edit_wooden_corners_bag_tape - Деревянные уголки + мешок + скотч\n"
                         "✔️ /edit_wooden_sheathing_bag_tape - Деревянная обрешетка + мешок + скотч\n"
                         "✔️ /edit_order_form - 🗒 Бланк заказа\n"
                         "✔️ /edit_bag_tape - Мешок + скотч\n"
                         "✔️ /edit_box_bag_tape - Коробка + мешок + скотч\n"
                         "✔️ /edit_pallet_crate - Паллет в обрешетке\n"
                         "✔️ /edit_pallet_with_a_solid_wooden_box - Паллет с глухим деревянным коробом\n"
                         "✔️ /edit_cargo_delivery_prices - Прайсы на доставку Карго\n"
                         "✔️ /edit_goods_redemption_service - Услуга Выкупа товаров\n"
                         "✔️ /edit_product_search_service - Услуга Поиска товаров (производителей в Китае)\n"
                         "✔️ /edit_supplier_inspection - Инспекция поставщиков по провинциям (выезд на производство)\n"
                         "✔️ /edit_wechat_registration_service - Услуга регистрации в WeChat\n"
                         "✔️ /edit_purchase_a_supplier_database - Приобрести базу данных поставщиков\n"
                         "✔️ /edit_what_payments_await_me - Какие платежи меня ожидают?\n"
                         "✔️ /edit_how_is_payment_made - Как совершается оплата?\n"
                         "✔️ /edit_self_redemption - 🛍 Самовыкуп\n"
                         "✔️ /edit_reviews - 💌 Отзывы\n"
                         "✔️ /edit_partnership_conditions_for_intermediaries_button - Партнерские условия для посредников"
                         "✔️ /edit_main_menu - текст меню бота\n"
                         "✔️ /edit_white_cargo_gte - Белая доставка грузов с ГТД\n\n"

                         "<b>Получение данных:</b>\n"
                         "✔️ /get_a_list_of_users_registered_in_the_bot - Получение списка зарегистрированных "
                         "пользователей\n"
                         "✔️ /get_users_who_launched_the_bot - Получение данных пользователей, запускающих бота\n\n"

                         "<b>Отправка сообщений:</b>\n"
                         "✔️ /send_an_image_to_bot_users - Отправка изображения через бота + текст\n"
                         "✔️ /send_a_message_to_bot_users - Отправка текста через бота\n\n"

                         "<b>Замена изображения постов и файлов:</b>\n"
                         "✔️ /greeting_photo - Пост приветствие\n"
                         "✔️ /get_price_lists_file - Замена Прейскуранта CFORB.xlsx"
                         "✔️ /services_and_prices_photo - Услуги и цены\n"
                         "✔️ /white_cargo_gte_photo - Белая доставка грузов с ГТД "
                         "✔️ /types_of_packaging_photo - Виды упаковки\n\n"

                         "/start - начальное меню\n", parse_mode="HTML")


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


@router.message(Command('get_a_list_of_users_registered_in_the_bot'))
async def export_data(message: types.Message, state: FSMContext):
    """Получение списка зарегистрированных пользователей"""
    await state.clear()  # Завершаем текущее состояние машины состояний
    try:
        if message.from_user.id not in [535185511, 301634256]:
            await message.reply('У вас нет доступа к этой команде.')
            return
        orders = reading_from_database()
        # Создание файла Excel
        workbook = create_excel_file(orders)
        filename = 'Зарегистрированные пользователи в боте.xlsx'
        workbook.save(filename)  # Сохранение файла
        text = ("Данные пользователей зарегистрированных в боте\n\n"
                "Для возврата в начальное меню нажми на /start или /help")
        file = FSInputFile(filename)
        await bot.send_document(message.from_user.id, document=file, caption=text)  # Отправка файла пользователю
        os.remove(filename)  # Удаление файла
    except Exception as e:
        logger.error(e)


def create_excel_file_start(orders):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    # Заголовки столбцов
    sheet['A1'] = 'ID аккаунта пользователя'
    sheet['B1'] = 'username'
    sheet['C1'] = 'Имя'
    sheet['D1'] = 'Фамилия'
    sheet['E1'] = 'Дата запуска бота'
    # Заполнение данными заказов
    for index, order in enumerate(orders, start=2):
        sheet.cell(row=index, column=1).value = order[0]  # ID аккаунта пользователя
        sheet.cell(row=index, column=2).value = order[1]  # username
        sheet.cell(row=index, column=3).value = order[2]  # Имя
        sheet.cell(row=index, column=4).value = order[3]  # Фамилия
        sheet.cell(row=index, column=5).value = order[4]  # Дата запуска бота

    return workbook


@router.message(Command("get_users_who_launched_the_bot"))
async def get_users_who_launched_the_bot(message: types.Message, state: FSMContext):
    """Получение данных пользователей, запускающих бота"""
    await state.clear()  # Завершаем текущее состояние машины состояний
    try:
        if message.from_user.id not in [535185511, 301634256]:
            await message.reply('У вас нет доступа к этой команде.')
            return
        orders = reading_from_database()
        workbook = create_excel_file_start(orders)  # Создание файла Excel
        filename = 'Данные пользователей запустивших бота.xlsx'
        workbook.save(filename)  # Сохранение файла
        file = FSInputFile(filename)
        text = ("Данные пользователей зарегистрированных в боте\n\n"
                "Для возврата в начальное меню нажми на /start или /help")
        await bot.send_document(message.from_user.id, document=file, caption=text)  # Отправка файла пользователю
        os.remove(filename)  # Удаление файла
    except Exception as e:
        logger.error(e)


class MyStates(StatesGroup):
    waiting_for_message = State()
    waiting_for_image = State()
    waiting_for_caption = State()


@router.callback_query(F.data == 'send_an_image_to_bot_users')
async def send_an_image_to_bot_users(message: types.Message, state: FSMContext):
    """Запрашивает изображение у администратора"""
    await state.clear()  # Завершаем текущее состояние машины состояний
    try:
        if message.from_user.id not in [535185511, 301634256]:
            await message.reply('У вас нет доступа к этой команде.')
            return
        await bot.send_message(message.from_user.id, text="Загрузите изображение для рассылки:")
        await state.set_state(MyStates.waiting_for_image)  # Устанавливаем состояние "ожидание изображения"
    except Exception as e:
        logger.error(e)


@router.message(StateFilter(MyStates.waiting_for_image))
async def process_send_image(message: types.Message, state: FSMContext):
    """
    Этот хендлер будет ждать загруженного изображения и переходить в состояние "ожидание подписи"
    """

    await state.update_data(photo=message.photo[-1].file_id)
    await bot.send_message(message.from_user.id, text="Введите подпись к изображению:")
    await state.set_state(MyStates.waiting_for_caption)


@router.message(StateFilter(MyStates.waiting_for_caption))
async def process_send_image_with_caption(message: types.Message, state: FSMContext):
    """
    Этот хендлер будет ждать введенной подписи и выполнять рассылку
    """
    state_data = await state.get_data()  # Получить данные о состоянии
    state_data['caption'] = message.text  # Сохраните заголовок в данных состояния
    photo = state_data.get('photo')  # Получите фотографию и подпись из государственных данных.
    caption = state_data.get('caption')
    user_ids = get_user_ids()  # Получаем список уникальных ID пользователей из базы данных
    if user_ids:
        for user_id in user_ids:  # Рассылка изображения с подписью всем пользователям из списка
            try:
                await bot.send_photo(user_id, photo, caption=caption)  # Отправляем изображение с подписью
            except Exception as e:
                print(f"Ошибка при отправке изображения с подписью пользователю {user_id}: {str(e)}")
    await message.answer("Изображение успешно разослано всем пользователям.")
    await state.clear()


@router.message(Command("send_a_message_to_bot_users"))
async def send_a_message_to_bot_users(message: types.Message, state: FSMContext):
    """Запрашивает текст сообщения у администратора"""
    await state.clear()  # Завершаем текущее состояние машины состояний
    try:
        if message.from_user.id not in [535185511, 301634256]:
            await message.reply('У вас нет доступа к этой команде.')
            return
        await bot.send_message(message.from_user.id, text="Введите текст для рассылки:")
        await state.set_state(MyStates.waiting_for_message)  # Устанавливаем состояние "ожидание сообщения"
    except Exception as e:
        logger.error(e)


@router.message(StateFilter(MyStates.waiting_for_message))
async def process_send_message(message: types.Message, state: FSMContext):
    """
    Этот хендлер будет ждать введенного текста и выполнять рассылку
    """
    # Получаем список уникальных ID пользователей из базы данных
    message_text = message.text
    user_ids = get_user_ids()
    if user_ids:
        for user_id in user_ids:  # Рассылка сообщения всем пользователям из списка
            try:
                await bot.send_message(chat_id=user_id, text=message_text, parse_mode="HTML")
            except Exception as e:
                print(f"Ошибка при отправке сообщения пользователю {user_id}: {str(e)}")
    await message.answer("Сообщение успешно разослано всем пользователям.")
    await state.clear()


def get_user_ids():
    """Получаем уникальные ID пользователей из базы данных"""
    try:
        conn = sqlite3.connect('your_database.db')  # Замените 'your_database.db' на имя вашей базы данных
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT user_id FROM users_start")
        user_ids = [row[0] for row in cursor.fetchall()]
        return user_ids
    except Exception as e:
        print(f"Ошибка при получении ID пользователей из базы данных: {str(e)}")
        return []


def register_admin_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(admin_send_start)
    dp.message.register(export_data)
    dp.message.register(get_users_who_launched_the_bot)
    dp.message.register(send_a_message_to_bot_users)
    dp.message.register(send_an_image_to_bot_users)
