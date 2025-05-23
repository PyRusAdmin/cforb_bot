from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message

from keyboards.user_keyboards.user_keyboards import create_packaging_keyboard, create_packaging_menu_keyboard
from states.states import (FormeditMainMenu)
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import router
from system.working_with_files import load_bot_info
from system.working_with_files import save_bot_info


@router.callback_query(F.data == "types_of_packaging")
async def types_of_packaging(callback_query: types.CallbackQuery, state: FSMContext):
    """Виды упаковки"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_media(
        media=InputMediaPhoto(media=FSInputFile('media/photos/types_of_packaging.jpg'),
                              caption=load_bot_info(messages="media/messages/types_of_packaging.json"),
                              parse_mode="HTML"),
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=create_packaging_keyboard(),
    )


# Обработчик команды /edit_types_of_packaging (только для админа)
@router.message(Command("edit_types_of_packaging"))
async def edit_useful_information(message: Message, state: FSMContext):
    """Редактирование: Виды упаковки"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_types_of_packaging)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_types_of_packaging)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text, file_path='media/messages/types_of_packaging.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "bag_tape")
async def bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Мешок + скотч"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/bag_tape.json"),
        reply_markup=create_packaging_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_bag_tape (только для админа)
@router.message(Command("edit_bag_tape"))
async def edit_bag_tape(message: Message, state: FSMContext):
    """Редактирование: Мешок + скотч"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_bag_tape)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_bag_tape)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text, file_path='media/messages/bag_tape.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "box_bag_tape")
async def box_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Коробка + мешок + скотч"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/box_bag_tape.json"),
        reply_markup=create_packaging_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_box_bag_tape (только для админа)
@router.message(Command("edit_box_bag_tape"))
async def edit_box_bag_tape(message: Message, state: FSMContext):
    """Редактирование: Коробка + мешок + скотч"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_box_bag_tape)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_box_bag_tape)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text, file_path='media/messages/box_bag_tape.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "wooden_sheathing_bag_tape")
async def wooden_sheathing_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянная обрешетка + мешок + скотч"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_media(
        media=InputMediaPhoto(
            media=FSInputFile('media/photos/types_of_packaging.jpg'),
            caption=load_bot_info(messages="media/messages/wooden_sheathing_bag_tape.json"),
            parse_mode="HTML"
        ),
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=create_packaging_menu_keyboard(),
    )


# Обработчик команды /edit_wooden_sheathing_bag_tape (только для админа)
@router.message(Command("edit_wooden_sheathing_bag_tape"))
async def edit_wooden_sheathing_bag_tape(message: Message, state: FSMContext):
    """Редактирование: Деревянная обрешетка + мешок + скотч"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_wooden_sheathing_bag_tape)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_wooden_sheathing_bag_tape)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text,
                  file_path='media/messages/wooden_sheathing_bag_tape.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "wooden_corners_bag_tape")
async def wooden_corners_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянные уголки + мешок + скотч"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/wooden_corners_bag_tape.json"),
        reply_markup=create_packaging_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_wooden_corners_bag_tape (только для админа)
@router.message(Command("edit_wooden_corners_bag_tape"))
async def edit_wooden_corners_bag_tape(message: Message, state: FSMContext):
    """Редактирование: Деревянные уголки + мешок + скотч"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_wooden_corners_bag_tape)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_wooden_corners_bag_tape)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text,
                  file_path='media/messages/wooden_corners_bag_tape.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "pallet_in_crate")
async def pallet_in_crate(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет в обрешетке"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/pallet_in_crate.json"),
        reply_markup=create_packaging_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_pallet_crate (только для админа)
@router.message(Command("edit_pallet_crate"))
async def edit_pallet_crate(message: Message, state: FSMContext):
    """Редактирование: Паллет в обрешетке"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_pallet_crate)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_pallet_crate)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text, file_path='media/messages/pallet_in_crate.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


""""_____________________________________________________________________________________"""


@router.callback_query(F.data == "pallet_with_a_solid_wooden_box")
async def pallet_with_a_solid_wooden_box(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет с глухим деревянным коробом"""
    await state.clear()  # Очищаем состояние
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=load_bot_info(messages="media/messages/pallet_with_a_solid_wooden_box.json"),
        reply_markup=create_packaging_menu_keyboard(),
        parse_mode="HTML"
    )


# Обработчик команды /edit_pallet_with_a_solid_wooden_box (только для админа)
@router.message(Command("edit_pallet_with_a_solid_wooden_box"))
async def edit_pallet_with_a_solid_wooden_box(message: Message, state: FSMContext):
    """Редактирование: Паллет с глухим деревянным коробом"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormeditMainMenu.edit_pallet_with_a_solid_wooden_box)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormeditMainMenu.edit_pallet_with_a_solid_wooden_box)
async def update_info(message: Message, state: FSMContext):
    save_bot_info(message.html_text,
                  file_path='media/messages/pallet_with_a_solid_wooden_box.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_types_of_packaging_handler():
    """Регистрируем handlers для бота"""
    router.message.register(types_of_packaging)
    router.message.register(bag_tape)
    router.message.register(box_bag_tape)
    router.message.register(wooden_sheathing_bag_tape)
    router.message.register(wooden_corners_bag_tape)
    router.message.register(pallet_in_crate)
    router.message.register(pallet_with_a_solid_wooden_box)
    router.message.register(edit_useful_information)  # редактирование: Виды упаковки
    router.message.register(edit_bag_tape)  # редактирование: Мешок + скотч
    router.message.register(edit_box_bag_tape)  # редактирование: Коробка + мешок + скотч
    router.message.register(edit_wooden_sheathing_bag_tape)  # Деревянная обрешетка + мешок + скотч
    router.message.register(edit_wooden_corners_bag_tape)  # Деревянные уголки + мешок + скотч
    router.message.register(edit_pallet_crate)  # Паллет в обрешетке
    router.message.register(edit_pallet_with_a_solid_wooden_box)  # Паллет в обрешетке
