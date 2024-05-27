from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto

from keyboards.user_keyboards.user_keyboards import create_packaging_keyboard, create_packaging_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info


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


def register_types_of_packaging_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(types_of_packaging)
    dp.message.register(bag_tape)
    dp.message.register(box_bag_tape)
    dp.message.register(wooden_sheathing_bag_tape)
    dp.message.register(wooden_corners_bag_tape)
    dp.message.register(pallet_in_crate)
    dp.message.register(pallet_with_a_solid_wooden_box)
