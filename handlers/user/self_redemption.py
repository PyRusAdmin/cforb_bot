from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from states.states import BotContentEditStates
from system.dispatcher import ADMIN_USER_ID, bot, router
from system.working_with_files import load_bot_info, save_bot_info


@router.callback_query(F.data == "self_redemption")
async def self_redemption(callback_query: types.CallbackQuery, state: FSMContext):
    """🛍 Самовыкуп"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/self_redemption.json"),
        reply_markup=create_main_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_self_redemption (только для админа)
@router.message(Command("edit_self_redemption"))
async def edit_self_redemption(message: Message, state: FSMContext):
    """Редактирование: 🛍 Самовыкуп"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(BotContentEditStates.edit_self_redemption)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(BotContentEditStates.edit_self_redemption)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text, file_path='media/messages/self_redemption.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_self_redemption_handler():
    """Регистрируем handlers для бота"""
    router.message.register(self_redemption)
    router.message.register(edit_self_redemption)
