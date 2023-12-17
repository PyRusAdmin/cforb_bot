from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "order_form")
async def order_form(callback_query: types.CallbackQuery, state: FSMContext):
    """Бланк заказа"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"<b>Скачайте и заполните наш фирменный бланк заказа, если возникнут какие-то вопросы, "
                            f"вы всегда можете обратиться к менеджеру @cargo_cfb.</b>\n\n"
                            f"Пароль к бланку - cforb\n\n"
                            f"<b>Связаться с менеджерами: @cargo_cfb</b>\n\n")
        main_menu_keyboard = create_main_menu_keyboard()
        with open('media/document/Бланк Заказа CFORB.xls', 'rb') as document:
            await bot.send_document(callback_query.from_user.id,  # ID пользователя
                                    caption=greeting_message,  # Текст для приветствия 👋
                                    document=document,
                                    reply_markup=main_menu_keyboard,
                                    parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_order_form_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(order_form)
