import sqlite3

from aiogram import types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from loguru import logger

from states.states import MyStates
from system.dispatcher import bot, router


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


@router.message(Command("send_an_image_to_bot_users"))
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
    user_ids = get_user_ids()
    if user_ids:
        for user_id in user_ids:  # Рассылка сообщения всем пользователям из списка
            try:
                await bot.send_message(chat_id=user_id, text=message.text, parse_mode="HTML")
            except Exception as e:
                print(f"Ошибка при отправке сообщения пользователю {user_id}: {str(e)}")
    await message.answer("Сообщение успешно разослано всем пользователям.")
    await state.clear()


def register_handlers_sending_messages():
    """Регистрация хендлеров для отправки сообщений и изображений"""
    router.message.register(process_send_image_with_caption, StateFilter(MyStates.waiting_for_caption))
    router.message.register(process_send_message, StateFilter(MyStates.waiting_for_message))
    router.message.register(process_send_image, StateFilter(MyStates.waiting_for_image))
    router.message.register(send_a_message_to_bot_users)
    router.callback_query.register(send_an_image_to_bot_users)
