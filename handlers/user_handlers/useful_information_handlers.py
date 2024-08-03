from aiogram import types, F
from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import bot, dp, ADMIN_USER_ID
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.callback_query(F.data == "useful_information")
async def useful_information(callback_query: types.CallbackQuery, state: FSMContext):
    """📚 Полезная информация"""

    await state.clear()  # Очищаем состояние
    data = load_bot_info(messages="media/messages/useful_information.json")
    main_menu_keyboard = create_main_menu_keyboard()
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_keyboard,
        parse_mode="HTML"
    )


class Formedit_useful_information(StatesGroup):
    text_edit_useful_information = State()


# Обработчик команды /edit_useful_information (только для админа)
@router.message(Command("edit_useful_information"))
async def edit_useful_information(message: Message, state: FSMContext):
    """Редактирование: Бланк заказа"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Formedit_useful_information.text_edit_useful_information)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_useful_information.text_edit_useful_information)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/useful_information.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_useful_information_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(useful_information)
    dp.message.register(edit_useful_information)
