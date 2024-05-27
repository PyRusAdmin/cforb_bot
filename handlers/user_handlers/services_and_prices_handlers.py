import json
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InputMediaPhoto
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_services_and_prices_keyboard, \
    create_services_and_prices_main_menu_keyboard
from system.dispatcher import bot, dp
from system.dispatcher import router


def load_bot_info(messages):
    with open(messages, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


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
        greeting_message = ()
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               # parse_mode=types.ParseMode.HTML
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
        # await state.finish()  # Завершаем текущее состояние машины состояний
        # await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/purchase_a_supplier_database.json")
        greeting_message = (
            f"<b>Поможем перевезти груз и пройти таможню без потерь времени и денег. Сделаем комплексную поставку: "
            f"подберем транспорт, соберем документы, подадим декларацию, оформим и привезем груз на склад. Или "
            f"подключимся на нужном этапе.</b>\n\n"
            f"• Поиск производства\n"
            f"• Выкуп товара\n"
            f"• Логистика\n"
            f"• Таможенное оформление, разрешительные документы\n"
            f"<b>Задать вопрос или передать заявку на расчет специалисту ВЭД: @cargo_cfb</b>\n\n")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        with open('media/photos/white_cargo_delivery_with_gas_turbine_engine.jpg', 'rb') as photo_file:
            await bot.send_photo(callback_query.from_user.id,  # ID пользователя
                                 caption=greeting_message,  # Текст для приветствия 👋
                                 photo=photo_file,
                                 reply_markup=main_menu_keyboard,
                                 # parse_mode=types.ParseMode.HTML
                                 )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "goods_redemption_service")
async def goods_redemption_service(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        # await state.finish()  # Завершаем текущее состояние машины состояний
        # await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/purchase_a_supplier_database.json")
        greeting_message = (f"Работаем только от 20 кг!\n\n"
                            f"✅ Выкуп товара (условия и комиссии)\n"
                            f"Вам необходимо предоставить ссылку на поставщика, товар с фото и характеристиками, "
                            f"предполагаемое количество.\n"
                            f"Что дальше?\n"
                            f"•	Мы формируем корзину по вашей заявке, передаём вам на проверку собранную заявку, Вы "
                            f"согласовываете выкуп, оплачиваете необходимую сумму, мы выкупаем!\n\n"
                            f"Комиссия за выкуп товара составит:\n"
                            f"•	Закуп до 3.000 ¥ - комиссия 8%\n"
                            f"•	Закуп 3.000 - 5.000 ¥ - комиссия 5%\n"
                            f"•	Закуп 5.000 - 10.000 ¥ - комиссия 4%\n"
                            f"•	Закуп 10.000 - 50.000 ¥ - комиссия 3%\n"
                            f"•	Закуп свыше 50.000 ¥ - комиссия 2%\n\n"
                            f"Минимальная сумма на выкуп 1000¥, минимальный вес груза на доставку через нас 20 кг.\n\n"
                            f"Что входит в комиссию:\n"
                            f"Формирование, размещение и оплата заказа, общение с поставщиком если есть какие-то "
                            f"трудности с заказом, согласовываем остатки с поставщиком (если поставщик не может "
                            f"выполнить заказ, формируем заявку на возврат), делаем фото и видео (из одной коробки - "
                            f"1 единица товара), хранение товара на складе до момента отправки.\n\n"
                            f"✅ Дополнительная услуга: наклейки со штрих кодами на товар для маркетплейсов от 100-300 "
                            f"шт 1 юань (по курсу).\n"
                            f"✅ Дополнительная услуга: проверка количества товара на соответствие, если выкупаете "
                            f"сами 1-2 юаня за 1 счетную единицу (зависит от упаковки товара).\n\n"
                            f"Если выкупаем Мы 0.5 - 1 юань (зависит от упаковки товара)\n"
                            f"❗️ Мы отвечаем за:\n"
                            f"* Выкуп товара согласно заявке\n"
                            f"* Доставку груза по всем трек-номерам на наш склад в Китае\n"
                            f"* Консолидацию груза\n"
                            f"* Упаковку груза согласно требованиям\n"
                            f"* Доставку груза в РФ (г. Москва)\n\n"
                            f"❗️ Работая с вашим поставщиком мы не несем ответственности за:\n"
                            f"* Качество его продукции\n"
                            f"* Срок обработки, изготовления и отправки товара поставщиками на наш склад в Китае\n"
                            f"* Бракованный товар - компания не проверяет товар на наличие явных и скрытых дефектов "
                            f"(Данную услугу можно запросить, оплачивается отдельно).\n"
                            f"* Цвет товара - цветопередача фотографии может отличаться от реального цвета товара. \n"
                            f"* Отправку поставщиком не того товара, который был заказан (если не заказана услуга "
                            f"проверки соответствия)\n"
                            f"* Отправку поставщиком товара другого размера\n\n"
                            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               # parse_mode=types.ParseMode.HTML
                               )  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@router.callback_query(F.data == "product_search_service")
async def product_search_service(callback_query: types.CallbackQuery, state: FSMContext):
    """📌 Кнопка “Услуга Поиска товаров (производителей в Китае)”"""
    try:
        # await state.finish()  # Завершаем текущее состояние машины состояний
        # await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/purchase_a_supplier_database.json")
        greeting_message = (f"<b>✅ Тарифы на поиск:</b>\n"
                            f"<i>Вам необходимо предоставить фото товара, характеристики, предполагаемое количество.</i>\n"
                            f"<i>Срок готовности ответа на запрос поиска, от 3 до 8 рабочих дней (в течение этого "
                            f"времени можем уточнять у Вас детали касающиеся товара, к примеру, если это фабрика, "
                            f"то товар можно будет изготовить прямо под Ваше техзадание).</i>\n\n"

                            f"<b>Не берем на поиск более двух товарных позиций за один раз, ищем 1-2 позиции, "
                            f"начинаем сотрудничество по ним, далее переходим к поиску других товаров.</b>\n\n"

                            f"Мы берём с Вас гарантийный платёж в размере: 1500₽\n\n"

                            f"<b>Для чего это нужно?</b>\n\n"

                            f"· Гарантийный платёж является нашим вознаграждением за потраченное время на поиски "
                            f"товара и общение с поставщиками в том случае, если Вы передумаете. Ведь в это время мы "
                            f"могли бы помочь другому клиенту с поиском и выкупом товара.\n\n"
                            f"<b>Что дальше?</b>\n\n"

                            f"· По результатам поиска мы предоставляем Вам подборку из лучших предложений (1-3 "
                            f"варианта).\n"
                            f"· Если Вы оформляете заказ, то сумма гарантийного платежа учитывается в стоимость "
                            f"оказанных услуг (таким образом, вычитаем из суммы за услуги внесенный ранее гарантийный "
                            f"платёж.).\n\n"

                            f"<b>Комиссия за поиск и выкуп товара составит:</b>\n\n"

                            f"· Закуп до 200.000 ₽. - комиссия 7%\n"
                            f"· Выше 200.000 ₽. - комиссия 5%\n"
                            f"· Свыше 1.000.000 ₽. - Комиссия 3%\n"
                            f"· Минимальная сумма заказа 100.000 ₽ и вес товара не менее 100 кг.\n"
                            f"· Доставка товара оплачивается отдельно, исходя из категории товара, определяется тариф "
                            f"на логистику.\n\n"

                            f"<b>📦 Проверка товара на брак и на количество:</b>\n"
                            f"Одна товарная позиция - одна единица товара фотоотчет, видеоотчет, осуществляется "
                            f"бесплатно по запросу. Всё что необходимо свыше, обговаривается индивидуально.\n\n"
                            f"<b>✅ Дополнительная услуга:</b> наклейки со штрих кодами на товар для маркетплейсов "
                            f"от 100-300 шт 1 юань (по курсу).\n"
                            f"<b>✅ Дополнительная услуга:</b> проверка количества товара на соответствие, 1-2 юаня "
                            f"за 1 счетную единицу (зависит от упаковки товара)\n\n"

                            f"<b>Связаться с менеджерами: @cargo_cfb</b>")
        main_menu_keyboard = create_services_and_prices_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               # parse_mode=types.ParseMode.HTML
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
