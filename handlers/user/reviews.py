from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from states.states import FormeditReviews
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.callback_query(F.data == "reviews")
async def reviews(callback_query: types.CallbackQuery, state: FSMContext):
    """💌 Отзывы"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/reviews.json"),
        reply_markup=create_main_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_reviews (только для админа)
@router.message(Command("edit_reviews"))
async def edit_reviews(message: Message, state: FSMContext):
    """Редактирование: 💌 Отзывы"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditReviews.text_edit_reviews)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditReviews.text_edit_reviews)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text, file_path='media/messages/reviews.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_reviews_handler():
    """Регистрируем handlers для бота"""
    router.message.register(reviews)
    router.message.register(edit_reviews)
