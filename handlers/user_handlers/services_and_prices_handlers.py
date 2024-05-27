from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_services_and_prices_keyboard, \
    create_services_and_prices_main_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router
from system.working_with_files import load_bot_info


@router.callback_query(F.data == "services_and_prices")
async def services_and_prices(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/services_and_prices.json")
        services_and_prices_keyboard = create_services_and_prices_keyboard()  # Клавиатуры поста приветствия 👋
        document = FSInputFile('media/photos/services_and_prices.jpg')
        media = InputMediaPhoto(media=document, caption=data)
        await bot.edit_message_media(media=media,
                                     chat_id=callback_query.message.chat.id,
                                     message_id=callback_query.message.message_id,
                                     reply_markup=services_and_prices_keyboard
                                     )
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "cargo_delivery_prices")
async def cargo_delivery_prices(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Прайсы на доставку Карго”"""
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/cargo_delivery_prices.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=data,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               )  # Текст в HTML-разметки
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('media/photos/price/1.png'), 'Прайс 1')
        media.attach_photo(types.InputFile('media/photos/price/2.png'), 'Прайс 2')
        media.attach_photo(types.InputFile('media/photos/price/3.png'), 'Прайс 3')
        await bot.send_media_group(callback_query.message.chat.id, media=media)
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "white_cargo_delivery_with_gas_turbine_engine")
async def white_cargo_delivery_with_gas_turbine_engine(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Белая доставка грузов с ГТД ”"""
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/white_cargo_delivery_with_gas_turbine_engine.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        with open('media/photos/white_cargo_delivery_with_gas_turbine_engine.jpg', 'rb') as photo_file:
            await bot.send_photo(callback_query.from_user.id,  # ID пользователя
                                 caption=data,  # Текст для приветствия 👋
                                 photo=photo_file,
                                 reply_markup=main_menu_keyboard,
                                 )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "goods_redemption_service")
async def goods_redemption_service(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/goods_redemption_service.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=data,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "product_search_service")
async def product_search_service(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Услуга Поиска товаров (производителей в Китае)”"""
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/product_search_service.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=data,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "supplier_inspection_by_province")
async def supplier_inspection_by_province(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Инспекция поставщиков по провинциям (выезд на производство)”"""
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/supplier_inspection_by_province.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=data,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "wechat_registration_service")
async def wechat_registration_service(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/wechat_registration_service.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=data,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "purchase_a_supplier_database")
async def purchase_a_supplier_database(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/purchase_a_supplier_database.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=data,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "what_payments_await_me")
async def what_payments_await_me(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Какие платежи меня ожидают?”"""
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/what_payments_await_me.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=data,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "how_is_payment_made")
async def how_is_payment_made(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Как совершается оплата?”"""
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/how_is_payment_made.json")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=data,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_services_and_prices_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(services_and_prices)
    dp.message.register(cargo_delivery_prices)
    dp.message.register(white_cargo_delivery_with_gas_turbine_engine)
    dp.message.register(goods_redemption_service)
    dp.message.register(product_search_service)
    dp.message.register(supplier_inspection_by_province)
    dp.message.register(wechat_registration_service)
    dp.message.register(purchase_a_supplier_database)
    dp.message.register(what_payments_await_me)
    dp.message.register(how_is_payment_made)
