import json
from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from loguru import logger

from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


# Загрузка информации из JSON-файла
def load_bot_info():
    with open("media/messages/order_form.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "order_form")
async def order_form(callback_query: types.CallbackQuery, state: FSMContext):
    """Бланк заказа"""
    try:
        await state.clear()  # Очищаем состояние

        main_menu_keyboard = create_main_menu_keyboard()
        data = load_bot_info()
        document = FSInputFile('media/document/Бланк Заказа CFORB.xls')

        await bot.send_document(chat_id=callback_query.message.chat.id, document=document,
                                reply_markup=main_menu_keyboard,
                                caption=data)
    except Exception as error:
        logger.exception(error)


def register_order_form_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(order_form)
