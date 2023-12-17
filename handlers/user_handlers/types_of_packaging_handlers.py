from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_packaging_keyboard, create_packaging_menu_keyboard
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "types_of_packaging")
async def types_of_packaging(callback_query: types.CallbackQuery, state: FSMContext):
    """Виды упаковки"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"<b>Здесь вы можете увидеть какие упаковки существуют, как выглядят, и сколько "
                            f"стоят.</b>\n\n"
                            
                            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        types_of_packaging_key = create_packaging_keyboard()
        with open('media/photos/types_of_packaging.jpg', 'rb') as photo_file:
            await bot.send_photo(callback_query.from_user.id,  # ID пользователя
                                 caption=greeting_message,  # Текст для приветствия 👋
                                 photo=photo_file,
                                 reply_markup=types_of_packaging_key,
                                 parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "bag_tape")
async def bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Мешок + скотч"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f'<a href="https://youtube.com/shorts/E2LFiy8iF0g">Мешок + скотч:</a> классические упаковка'
                            f' с использованием мешка и упаковочного '
                            f'скотча, подходит для текстиля и мягких товаров.\n\n'
                            f'<b>Стоимость данной упаковки 5$ место</b>\n\n'
                            f'<b>Связаться с менеджерами: @cargo_cfb</b>')
        types_of_packaging_key = create_packaging_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "box_bag_tape")
async def box_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Коробка + мешок + скотч"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (
            f'<a href="https://youtube.com/shorts/DX-EFbUkOf8"> Коробка + мешок + скотч: </a>если у вас '
            f'много разных товаров в том числе маленькие коробочки, весь товар складывается в нашу '
            f'коробку, далее упаковка в мешок и упаковочный скотч.\n\n'
            f'<b>Стоимость данной упаковки 8$ место</b>\n\n'
            f'<b>Связаться с менеджерами: @cargo_cfb</b>')
        types_of_packaging_key = create_packaging_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "wooden_sheathing_bag_tape")
async def wooden_sheathing_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянная обрешетка + мешок + скотч"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f'<a href="https://youtube.com/shorts/4ogIlLQUipc">Деревянная обрешетка + мешок + '
                            f'скотч:</a> Каркас из деревянных решеток (досок, брусьев), который способствует хорошей '
                            f'фиксации груза и его защите от механических повреждений. Применяется для упаковки '
                            f'хрупкого и бьющегося товара. + мешок + скотч\n\n'
                            f'<b>Стоимость данной упаковки 10$ место</b>\n\n'
                            f'<b>Связаться с менеджерами: @cargo_cfb</b>')
        types_of_packaging_key = create_packaging_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "wooden_corners_bag_tape")
async def wooden_corners_bag_tape(callback_query: types.CallbackQuery, state: FSMContext):
    """Деревянные уголки + мешок + скотч"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f'<a href="https://youtube.com/shorts/QcXqjaESW7s">Уголки + мешок + скотч:</a> Легче чем '
                            f'обрешетка, держит форму коробки, но менее защищенная, т.к '
                            f'практически полностью открытая.\n\n'
                            f'<b>Стоимость данной упаковки 10$ место</b>\n\n'
                            f'<b>Связаться с менеджерами: @cargo_cfb</b>\n\n')
        types_of_packaging_key = create_packaging_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "pallet_in_crate")
async def pallet_in_crate(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет в обрешетке"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f'<a href="https://youtube.com/shorts/QcXqjaESW7s">Паллет в обрешетке:</a> '
                            f'Вид упаковки используется для крупногабаритных или хрупких грузов, представляет из себя '
                            f'поддон с деревянными бортами как у обрешетки. Погрузочно-разгрузочные работы '
                            f'товаров, упакованных таким образом, осуществляются при помощи вилочного погрузчика.\n\n'
                            f'<b>Стоимость данной упаковки 45$ за куб</b>\n\n'
                            f'<b>Связаться с менеджерами: @cargo_cfb</b>')
        types_of_packaging_key = create_packaging_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=types_of_packaging_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "pallet_with_a_solid_wooden_box")
async def pallet_with_a_solid_wooden_box(callback_query: types.CallbackQuery, state: FSMContext):
    """Паллет с глухим деревянным коробом"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
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
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_types_of_packaging_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(types_of_packaging)
    dp.register_message_handler(bag_tape)
    dp.register_message_handler(box_bag_tape)
    dp.register_message_handler(wooden_sheathing_bag_tape)
    dp.register_message_handler(wooden_corners_bag_tape)
    dp.register_message_handler(pallet_in_crate)
    dp.register_message_handler(pallet_with_a_solid_wooden_box)
