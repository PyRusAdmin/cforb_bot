import os

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_packaging_keyboard, create_packaging_menu_keyboard
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.message(Command("types_of_packaging_photo"))
async def types_of_packaging_photo(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Пожалуйста, отправьте новое фото для замены в формате jpg")


@router.message(F.photo)
async def replace_photo(message: types.Message):
    # Получаем файл фотографии
    photo = message.photo[-1]
    file_info = await message.bot.get_file(photo.file_id)
    new_photo_path = os.path.join("media/photos/", 'types_of_packaging.jpg')
    # Загружаем файл на диск
    await message.bot.download_file(file_info.file_path, new_photo_path)
    await message.answer("Фото успешно заменено!")


@router.callback_query(F.data == "types_of_packaging")
async def types_of_packaging(callback_query: types.CallbackQuery, state: FSMContext):
    """Виды упаковки"""
    await state.clear()  # Очищаем состояние
    data = load_bot_info(messages="media/messages/types_of_packaging.json")
    document = FSInputFile('media/photos/types_of_packaging.jpg')
    types_of_packaging_key = create_packaging_keyboard()
    media = InputMediaPhoto(media=document, caption=data)
    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=types_of_packaging_key
                                 )


class Formeedit_types_of_packaging(StatesGroup):
    text_edit_types_of_packaging = State()


# Обработчик команды /edit_types_of_packaging (только для админа)
@router.message(Command("edit_types_of_packaging"))
async def edit_useful_information(message: Message, state: FSMContext):
    """Редактирование: Виды упаковки"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(Formeedit_types_of_packaging.text_edit_types_of_packaging)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formeedit_types_of_packaging.text_edit_types_of_packaging)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/types_of_packaging.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "bag_tape")
async def bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Мешок + скотч"""
    await state.clear()  # Очищаем состояние
    types_of_packaging_key = create_packaging_menu_keyboard()
    data = load_bot_info(messages="media/messages/bag_tape.json")
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=types_of_packaging_key
    )


class Formedit_bag_tape(StatesGroup):
    text_edit_bag_tape = State()


# Обработчик команды /edit_bag_tape (только для админа)
@router.message(Command("edit_bag_tape"))
async def edit_bag_tape(message: Message, state: FSMContext):
    """Редактирование: Мешок + скотч"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(Formedit_bag_tape.text_edit_bag_tape)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_bag_tape.text_edit_bag_tape)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/bag_tape.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "box_bag_tape")
async def box_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Коробка + мешок + скотч"""
    await state.clear()  # Очищаем состояние
    types_of_packaging_key = create_packaging_menu_keyboard()
    data = load_bot_info(messages="media/messages/box_bag_tape.json")
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=types_of_packaging_key
    )


class Formeedit_box_bag_tape(StatesGroup):
    text_edit_box_bag_tape = State()


# Обработчик команды /edit_box_bag_tape (только для админа)
@router.message(Command("edit_box_bag_tape"))
async def edit_box_bag_tape(message: Message, state: FSMContext):
    """Редактирование: Коробка + мешок + скотч"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(Formeedit_box_bag_tape.text_edit_box_bag_tape)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formeedit_box_bag_tape.text_edit_box_bag_tape)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/box_bag_tape.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "wooden_sheathing_bag_tape")
async def wooden_sheathing_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянная обрешетка + мешок + скотч"""
    await state.clear()  # Очищаем состояние
    types_of_packaging_key = create_packaging_menu_keyboard()
    document = FSInputFile('media/photos/types_of_packaging.jpg')
    data = load_bot_info(messages="media/messages/wooden_sheathing_bag_tape.json")
    media = InputMediaPhoto(media=document, caption=data)
    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=types_of_packaging_key
                                 )


class Formedit_wooden_sheathing_bag_tape(StatesGroup):
    text_edit_wooden_sheathing_bag_tape = State()


# Обработчик команды /edit_wooden_sheathing_bag_tape (только для админа)
@router.message(Command("edit_wooden_sheathing_bag_tape"))
async def edit_wooden_sheathing_bag_tape(message: Message, state: FSMContext):
    """Редактирование: Деревянная обрешетка + мешок + скотч"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(Formedit_wooden_sheathing_bag_tape.text_edit_wooden_sheathing_bag_tape)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_wooden_sheathing_bag_tape.text_edit_wooden_sheathing_bag_tape)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/wooden_sheathing_bag_tape.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "wooden_corners_bag_tape")
async def wooden_corners_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянные уголки + мешок + скотч"""
    await state.clear()  # Очищаем состояние
    data = load_bot_info(messages="media/messages/wooden_corners_bag_tape.json")

    types_of_packaging_key = create_packaging_menu_keyboard()
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=types_of_packaging_key
    )


class Formedit_wooden_corners_bag_tape(StatesGroup):
    text_edit_wooden_corners_bag_tape = State()


# Обработчик команды /edit_wooden_corners_bag_tape (только для админа)
@router.message(Command("edit_wooden_corners_bag_tape"))
async def edit_wooden_corners_bag_tape(message: Message, state: FSMContext):
    """Редактирование: Деревянные уголки + мешок + скотч"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(Formedit_wooden_corners_bag_tape.text_edit_wooden_corners_bag_tape)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_wooden_corners_bag_tape.text_edit_wooden_corners_bag_tape)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/wooden_corners_bag_tape.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "pallet_in_crate")
async def pallet_in_crate(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет в обрешетке"""
    await state.clear()  # Очищаем состояние
    data = load_bot_info(messages="media/messages/pallet_in_crate.json")
    types_of_packaging_key = create_packaging_menu_keyboard()
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=types_of_packaging_key
    )


class Formedit_pallet_crate(StatesGroup):
    text_edit_pallet_crate = State()


# Обработчик команды /edit_pallet_crate (только для админа)
@router.message(Command("edit_pallet_crate"))
async def edit_pallet_crate(message: Message, state: FSMContext):
    """Редактирование: Паллет в обрешетке"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(Formedit_pallet_crate.text_edit_pallet_crate)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_pallet_crate.text_edit_pallet_crate)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/pallet_in_crate.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "pallet_with_a_solid_wooden_box")
async def pallet_with_a_solid_wooden_box(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет с глухим деревянным коробом"""
    await state.clear()  # Очищаем состояние
    data = load_bot_info(messages="media/messages/pallet_with_a_solid_wooden_box.json")
    types_of_packaging_key = create_packaging_menu_keyboard()
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=types_of_packaging_key
    )


class Formedit_pallet_with_a_solid_wooden_box(StatesGroup):
    text_edit_pallet_with_a_solid_wooden_box = State()


# Обработчик команды /edit_pallet_with_a_solid_wooden_box (только для админа)
@router.message(Command("edit_pallet_with_a_solid_wooden_box"))
async def edit_pallet_with_a_solid_wooden_box(message: Message, state: FSMContext):
    """Редактирование: Паллет с глухим деревянным коробом"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(Formedit_pallet_with_a_solid_wooden_box.text_edit_pallet_with_a_solid_wooden_box)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_pallet_with_a_solid_wooden_box.text_edit_pallet_with_a_solid_wooden_box)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info,
                  file_path='media/messages/pallet_with_a_solid_wooden_box.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_types_of_packaging_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(types_of_packaging)
    dp.message.register(bag_tape)
    dp.message.register(box_bag_tape)
    dp.message.register(wooden_sheathing_bag_tape)
    dp.message.register(wooden_corners_bag_tape)
    dp.message.register(pallet_in_crate)
    dp.message.register(pallet_with_a_solid_wooden_box)
    dp.message.register(edit_useful_information)  # редактирование: Виды упаковки
    dp.message.register(edit_bag_tape)  # редактирование: Мешок + скотч
    dp.message.register(edit_box_bag_tape)  # редактирование: Коробка + мешок + скотч
    dp.message.register(edit_wooden_sheathing_bag_tape)  # Деревянная обрешетка + мешок + скотч
    dp.message.register(edit_wooden_corners_bag_tape)  # Деревянные уголки + мешок + скотч
    dp.message.register(edit_pallet_crate)  # Паллет в обрешетке
    dp.message.register(edit_pallet_with_a_solid_wooden_box)  # Паллет в обрешетке
    """Редактирование фото"""
    dp.message.register(types_of_packaging_photo)  # Паллет в обрешетке
