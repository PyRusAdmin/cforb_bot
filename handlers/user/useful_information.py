from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from states.states import FormeditUsefulInformation
from system.dispatcher import bot, dp, ADMIN_USER_ID
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.callback_query(F.data == "useful_information")
async def useful_information(callback_query: types.CallbackQuery, state: FSMContext):
    """📚 Полезная информация"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/useful_information.json"),
        reply_markup=create_main_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_useful_information (только для админа)
@router.message(Command("edit_useful_information"))
async def edit_useful_information(message: Message, state: FSMContext):
    """Редактирование: Бланк заказа"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(FormeditUsefulInformation.text_edit_useful_information)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditUsefulInformation.text_edit_useful_information)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text, file_path='media/messages/useful_information.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_useful_information_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(useful_information)
    dp.message.register(edit_useful_information)
