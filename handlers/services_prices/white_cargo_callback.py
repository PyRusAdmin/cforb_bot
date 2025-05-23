import os

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_services_and_prices_main_menu_keyboard
from states.states import EditWhiteCargoDeliveryState
from system.dispatcher import ADMIN_USER_ID, bot, router
from system.working_with_files import load_bot_info, save_bot_info


@router.callback_query(F.data == "white_cargo_gte")
async def handle_white_cargo_callback(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Белая доставка грузов с ГТД ”"""
    try:
        await state.clear()  # Очищаем состояние
        await bot.edit_message_media(
            media=InputMediaPhoto(
                media=FSInputFile('media/photos/white_cargo_gte.jpg'),
                caption=load_bot_info(messages="media/messages/services_prices_messages/white_cargo_gte.json"),
                parse_mode="HTML"
            ),
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=create_services_and_prices_main_menu_keyboard(),
        )
    except Exception as error:
        logger.exception(error)


# Обработчик команды /edit_white_cargo_gte (только для админа)
@router.message(Command("edit_white_cargo_gte"))
async def cmd_edit_white_cargo_text(message: Message, state: FSMContext):
    """Редактирование: Белая доставка грузов с ГТД"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(EditWhiteCargoDeliveryState.edit_text)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(EditWhiteCargoDeliveryState.edit_text)
async def update_white_cargo_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text, file_path='media/messages/services_prices_messages/white_cargo_gte.json')
    await message.reply("Информация обновлена.")
    await state.clear()


def register_handle_white_cargo_callback():
    """Регистрируем handlers для бота"""
    router.message.register(handle_white_cargo_callback)
    router.message.register(cmd_edit_white_cargo_text)
    router.message.register(update_white_cargo_info)
