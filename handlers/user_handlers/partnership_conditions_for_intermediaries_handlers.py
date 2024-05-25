import json

from aiogram import types, F

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router


# Загрузка информации из JSON-файла
def load_bot_info():
    with open("media/messages/partnership_conditions_for_intermediaries_button.json", 'r',
              encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "partnership_conditions_for_intermediaries_button")
async def partnership_conditions_for_intermediaries(callback_query: types.CallbackQuery):
    """Партнерские условия для посредников"""
    data = load_bot_info()
    main_menu_keyboard = create_main_menu_keyboard()

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_keyboard
    )


def register_partnership_conditions_for_intermediaries_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(partnership_conditions_for_intermediaries)
