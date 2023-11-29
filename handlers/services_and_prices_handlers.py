from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards import services_and_prices_key
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "services_and_prices")
async def services_and_prices(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        from_user_name = callback_query.from_user.first_name  # Получаем фамилию пользователя
        greeting_message = f"{from_user_name}, ознакомьтесь с нашими услугами и ценами!\n\n"
        services_and_prices_keyboard = services_and_prices_key()  # Клавиатуры поста приветствия 👋
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=services_and_prices_keyboard,  # Клавиатура приветствия 👋
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_services_and_prices_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(services_and_prices)
