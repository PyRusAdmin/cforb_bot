from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.callback_query(F.data == "reviews")
async def reviews(callback_query: types.CallbackQuery, state: FSMContext):
    """💌 Отзывы"""
    await state.clear()  # Очищаем состояние
    data = load_bot_info(messages="media/messages/reviews.json")
    main_menu_keyboard = create_main_menu_keyboard()

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_keyboard
    )


class Formedit_reviews(StatesGroup):
    text_edit_reviews = State()


# Обработчик команды /edit_reviews (только для админа)
@router.message(Command("edit_reviews"))
async def edit_reviews(message: Message, state: FSMContext):
    """Редактирование: 💌 Отзывы"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(Formedit_reviews.text_edit_reviews)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_reviews.text_edit_reviews)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/reviews.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_reviews_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(reviews)
    dp.message.register(edit_reviews)
