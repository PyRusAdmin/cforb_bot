import json

from aiogram import types, F
from aiogram.fsm.context import FSMContext

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router


def load_bot_info():
    with open("media/messages/reviews.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "reviews")
async def reviews(callback_query: types.CallbackQuery, state: FSMContext):
    """💌 Отзывы"""
    await state.clear()  # Очищаем состояние
    data = load_bot_info()
    main_menu_keyboard = create_main_menu_keyboard()

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_keyboard
    )


def register_reviews_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(reviews)
