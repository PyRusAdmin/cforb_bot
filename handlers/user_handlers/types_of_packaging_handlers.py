import json

from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_packaging_keyboard, create_packaging_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router


# Загрузка информации из JSON-файла
def load_bot_info():
    with open("media/messages/types_of_packaging.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "types_of_packaging")
async def types_of_packaging(callback_query: types.CallbackQuery, state: FSMContext):
    """Виды упаковки"""
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info()
        document = FSInputFile('media/photos/types_of_packaging.jpg')
        types_of_packaging_key = create_packaging_keyboard()
        media = InputMediaPhoto(media=document, caption=data)
        await bot.edit_message_media(media=media,
                                     chat_id=callback_query.message.chat.id,
                                     message_id=callback_query.message.message_id,
                                     reply_markup=types_of_packaging_key
                                     )
    except Exception as error:
        logger.exception(error)


# Загрузка информации из JSON-файла
def load_bot_infos():
    with open("media/messages/bag_tape.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "bag_tape")
async def bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Мешок + скотч"""
    try:
        await state.clear()  # Очищаем состояние
        types_of_packaging_key = create_packaging_menu_keyboard()
        document = FSInputFile('media/photos/types_of_packaging.jpg')
        data = load_bot_infos()
        media = InputMediaPhoto(media=document, caption=data)
        await bot.edit_message_media(media=media,
                                     chat_id=callback_query.message.chat.id,
                                     message_id=callback_query.message.message_id,
                                     reply_markup=types_of_packaging_key
                                     )
    except Exception as error:
        logger.exception(error)


# Загрузка информации из JSON-файла
def load_bot_infoss():
    with open("media/messages/box_bag_tape.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "box_bag_tape")
async def box_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Коробка + мешок + скотч"""
    try:
        await state.clear()  # Очищаем состояние
        types_of_packaging_key = create_packaging_menu_keyboard()
        document = FSInputFile('media/photos/types_of_packaging.jpg')
        data = load_bot_infoss()
        media = InputMediaPhoto(media=document, caption=data)
        await bot.edit_message_media(media=media,
                                     chat_id=callback_query.message.chat.id,
                                     message_id=callback_query.message.message_id,
                                     reply_markup=types_of_packaging_key
                                     )
    except Exception as error:
        logger.exception(error)


# Загрузка информации из JSON-файла
def load_bot_infosss():
    with open("media/messages/wooden_sheathing_bag_tape.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "wooden_sheathing_bag_tape")
async def wooden_sheathing_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянная обрешетка + мешок + скотч"""
    try:
        await state.clear()  # Очищаем состояние
        types_of_packaging_key = create_packaging_menu_keyboard()
        document = FSInputFile('media/photos/types_of_packaging.jpg')
        data = load_bot_infosss()
        media = InputMediaPhoto(media=document, caption=data)
        await bot.edit_message_media(media=media,
                                     chat_id=callback_query.message.chat.id,
                                     message_id=callback_query.message.message_id,
                                     reply_markup=types_of_packaging_key
                                     )
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "wooden_corners_bag_tape")
async def wooden_corners_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянные уголки + мешок + скотч"""
    try:
        await state.clear()  # Очищаем состояние
        greeting_message = (f'<a href="https://youtube.com/shorts/QcXqjaESW7s">Уголки + мешок + скотч:</a> Легче чем '
                            f'обрешетка, держит форму коробки, но менее защищенная, т.к '
                            f'практически полностью открытая.\n\n'
                            f'<b>Стоимость данной упаковки 10$ место</b>\n\n'
                            f'<b>Связаться с менеджерами: @cargo_cfb</b>\n\n')
        types_of_packaging_key = create_packaging_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "pallet_in_crate")
async def pallet_in_crate(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет в обрешетке"""
    try:
        # await state.finish()  # Завершаем текущее состояние машины состояний
        # await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        await state.clear()  # Очищаем состояние
        greeting_message = (f'<a href="https://www.youtube.com/shorts/Z2awci-nCNk">Паллет в обрешетке:</a> '
                            f'Вид упаковки используется для крупногабаритных или хрупких грузов, представляет из себя '
                            f'поддон с деревянными бортами как у обрешетки. Погрузочно-разгрузочные работы '
                            f'товаров, упакованных таким образом, осуществляются при помощи вилочного погрузчика.\n\n'
                            f'<b>Стоимость данной упаковки 45$ за куб</b>\n\n'
                            f'<b>Связаться с менеджерами: @cargo_cfb</b>')
        types_of_packaging_key = create_packaging_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               # parse_mode=types.ParseMode.HTML
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "pallet_with_a_solid_wooden_box")
async def pallet_with_a_solid_wooden_box(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет с глухим деревянным коробом"""
    try:
        # await state.finish()  # Завершаем текущее состояние машины состояний
        # await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        await state.clear()  # Очищаем состояние
        greeting_message = (f"<b>Паллет с глухим деревянным коробом:</b> Вид упаковки используется для крупногабаритных"
                            f" или хрупких грузов, представляет из себя поддон с деревянными бортами как у обрешетки. "
                            f"Погрузочно-разгрузочные работы товаров, упакованных таким образом, осуществляются при "
                            f"помощи вилочного погрузчика.\n\n"

                            f"<b>Стоимость данной упаковки 90-100$ за куб</b>\n\n"

                            f"<b>Связаться с менеджерами: @cargo_cfb</b>\n\n")
        types_of_packaging_key = create_packaging_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_types_of_packaging_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(types_of_packaging)
    dp.message.register(bag_tape)
    dp.message.register(box_bag_tape)
    dp.message.register(wooden_sheathing_bag_tape)
    dp.message.register(wooden_corners_bag_tape)
    dp.message.register(pallet_in_crate)
    dp.message.register(pallet_with_a_solid_wooden_box)
