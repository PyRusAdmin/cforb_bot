import os

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_services_and_prices_main_menu_keyboard
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.message(Command("white_cargo_gte_photo"))
async def cmd_replace_white_cargo_photo(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Пожалуйста, отправьте новое фото для замены в формате jpg")


@router.message(F.photo)
async def handle_photo_upload(message: types.Message):
    # Получаем файл фотографии
    photo = message.photo[-1]
    file_info = await message.bot.get_file(photo.file_id)
    new_photo_path = os.path.join("media/photos/", 'white_cargo_gte.jpg')
    # Загружаем файл на диск
    await message.bot.download_file(file_info.file_path, new_photo_path)
    await message.answer("Фото успешно заменено!")


@router.callback_query(F.data == "white_cargo_gte")
async def handle_white_cargo_callback(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Белая доставка грузов с ГТД ”"""
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/services_prices_messages/white_cargo_gte.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        document = FSInputFile('media/photos/white_cargo_gte.jpg')
        media = InputMediaPhoto(media=document, caption=data, parse_mode="HTML")
        await bot.edit_message_media(
            media=media,
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=main_menu_keyboard,
        )
    except Exception as error:
        logger.exception(error)


class EditWhiteCargoDeliveryState(StatesGroup):
    edit_text = State()


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
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/services_prices_messages/white_cargo_gte.json')
    await message.reply("Информация обновлена.")
    await state.clear()


def register_handle_white_cargo_callback():
    """Регистрируем handlers для бота"""
    dp.message.register(handle_white_cargo_callback)
    dp.message.register(cmd_edit_white_cargo_text)
    dp.message.register(update_white_cargo_info)
    dp.message.register(cmd_replace_white_cargo_photo)
