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


@router.callback_query(F.data == "partnership_conditions_for_intermediaries_button")
async def partnership_conditions_for_intermediaries(callback_query: types.CallbackQuery):
    """Партнерские условия для посредников"""
    data = load_bot_info(messages="media/messages/partnership_conditions_for_intermediaries_button.json")
    main_menu_keyboard = create_main_menu_keyboard()

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_keyboard
    )

class Formedit_partnership_conditions_for_intermediaries_button(StatesGroup):
    text_edit_partnership_conditions_for_intermediaries_button = State()


# Обработчик команды /edit_partnership_conditions_for_intermediaries_button (только для админа)
@router.message(Command("edit_partnership_conditions_for_intermediaries_button"))
async def edit_partnership_conditions_for_intermediaries_button(message: Message, state: FSMContext):
    """Редактирование: Партнерские условия для посредников"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(Formedit_partnership_conditions_for_intermediaries_button.text_edit_partnership_conditions_for_intermediaries_button)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_partnership_conditions_for_intermediaries_button.text_edit_partnership_conditions_for_intermediaries_button)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/partnership_conditions_for_intermediaries_button.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()

def register_partnership_conditions_for_intermediaries_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(partnership_conditions_for_intermediaries)
    dp.message.register(edit_partnership_conditions_for_intermediaries_button)
