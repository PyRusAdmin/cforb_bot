from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def get_price_lists_keyboard():
    rows = [
        [InlineKeyboardButton(text='Назад к ⭐️ Услуги и цены', callback_data='services_and_prices')],
        [InlineKeyboardButton(text='Получить прайсы', callback_data='get_price_lists')],
        [InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')],
    ]
    packaging_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return packaging_menu_keyboard


def create_packaging_menu_keyboard():
    """
    Создает клавиатуру для выбора видов упаковки.
    Кнопка "Назад к упаковкам" возвращает к предыдущему меню ('types_of_packaging').
    Кнопка "Главное меню" возвращает к главному меню ('main_menu').
    """
    rows = [
        [InlineKeyboardButton(text='Назад к упаковкам', callback_data='types_of_packaging')],
        [InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')],
    ]
    packaging_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return packaging_menu_keyboard


def create_packaging_keyboard():
    """
    Создаем клавиатуру для видов упаковки
    Кнопка "Мешок + скотч" ('bag_tape')
    Кнопка "Коробка + мешок + скотч" ('box_bag_tape')
    Кнопка "Деревянная обрешетка + мешок + скотч" ('wooden_sheathing_bag_tape')
    Кнопка "Деревянные уголки + мешок + скотч" ('wooden_corners_bag_tape')
    Кнопка "Паллет в обрешетке" ('pallet_in_crate')
    Кнопка "Паллет с глухим деревянным коробом" ('pallet_with_hollow_box')
    Кнопка "Главное меню" возвращает к главному меню ('main_menu').
    """
    rows = [
        # packaging_keyboard = InlineKeyboardMarkup()
        [InlineKeyboardButton(text='Мешок + скотч', callback_data='bag_tape')],
        [InlineKeyboardButton(text='Коробка + мешок + скотч', callback_data='box_bag_tape')],
        [InlineKeyboardButton(text='Деревянная обрешетка + мешок + скотч', callback_data='wooden_sheathing_bag_tape')],
        [InlineKeyboardButton(text='Деревянные уголки + мешок + скотч', callback_data='wooden_corners_bag_tape')],
        [InlineKeyboardButton(text='Паллет в обрешетке', callback_data='pallet_in_crate')],
        [InlineKeyboardButton(text='Паллет с глухим деревянным коробом',
                              callback_data='pallet_with_a_solid_wooden_box')],
        [InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')],
    ]
    packaging_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return packaging_keyboard


def create_greeting_keyboard():
    """
    Создаем клавиатуру для приветственного сообщения 👋
    Кнопка "Услуги и цены" ('services_and_prices')
    Кнопка "Бланк заказа" ('order_form')
    Кнопка "Самовыкуп" ('self_redemption')
    Кнопка "Партнерка" ('partnership_conditions_for_intermediaries_button')
    Кнопка "Виды упаковки" ('types_of_packaging')
    Кнопка "Отзывы" ('reviews')
    Кнопка "Полезная информация" ('useful_information')
    Кнопка "Связаться с менеджером" ('contact_manager')
    """
    rows = [
        [InlineKeyboardButton(text='⭐️ Услуги и цены', callback_data='services_and_prices'),
         InlineKeyboardButton(text='💰 Партнерка', callback_data="partnership_conditions_for_intermediaries_button")],
        [InlineKeyboardButton(text='🗒 Бланк заказа', callback_data='order_form'),
         InlineKeyboardButton(text='🛍 Самовыкуп', callback_data="self_redemption")],
        [InlineKeyboardButton(text='📦 Виды упаковки', callback_data='types_of_packaging'),
         InlineKeyboardButton(text='💌 Отзывы', callback_data='reviews')],
        [InlineKeyboardButton(text='📚 Полезная информация', callback_data='useful_information')],
        [InlineKeyboardButton(text="📞 Связаться с менеджером", url='https://t.me/cargo_cfb')]
    ]
    greeting_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return greeting_keyboard


def create_services_and_prices_keyboard():
    """
    Создает клавиатуру для раздела 'Услуги и цены'
    Кнопка "Прайсы на доставку Карго" ('cargo_delivery_prices')
    Кнопка "Белая доставка грузов с ГТД" ('white_cargo_delivery_with_gas_turbine_engine')
    Кнопка "Услуга Выкупа товаров" ('goods_redemption')
    Кнопка "Услуга Поиска товаров (производителей в Китае)" ('goods_search_service')
    Кнопка "Инспекция поставщиков по провинциям (выезд на производство)" ('inspection_service')
    Кнопка "Услуга регистрации WeChat" ('wechat_registration_service')
    Кнопка "Приобрести базу поставщиков" ('purchase_of_the_base_of_suppliers')
    Кнопка "Какие платежи меня ожидают?" ('how_many_payments_will_i_expect')
    Кнопка "Как совершается оплата?" ('how_to_make_a_payment')
    Кнопка "Главное меню" ('main_menu')
    """
    rows = [
        [InlineKeyboardButton(text='Прайсы на доставку Карго', callback_data='cargo_delivery_prices')],
        [InlineKeyboardButton(text='Белая доставка грузов с ГТД',
                              callback_data='white_cargo_delivery_with_gas_turbine_engine')],
        [InlineKeyboardButton(text='Услуга Выкупа товаров', callback_data='goods_redemption_service')],
        [InlineKeyboardButton(text='Услуга Поиска товаров (производителей в Китае)',
                              callback_data='product_search_service')],
        [InlineKeyboardButton(text='Инспекция поставщиков по провинциям (выезд на производство)',
                              callback_data='supplier_inspection_by_province')],
        [InlineKeyboardButton(text='Услуга регистрации WeChat', callback_data='wechat_registration_service')],
        [InlineKeyboardButton(text='Приобрести базу поставщиков', callback_data='purchase_a_supplier_database')],
        [InlineKeyboardButton(text='Какие платежи меня ожидают?', callback_data='what_payments_await_me')],
        [InlineKeyboardButton(text='Как совершается оплата?', callback_data='how_is_payment_made')],
        [InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')],
    ]
    services_and_prices_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)

    return services_and_prices_keyboard


def create_services_and_prices_main_menu_keyboard():
    """Создает клавиатуру для кнопки 'Главное меню' из раздела 'Услуги и цены'"""
    rows = [
        [InlineKeyboardButton(text='Назад к услугам', callback_data="services_and_prices")],
        [InlineKeyboardButton(text='↩️Главное меню', callback_data="main_menu")],
    ]
    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_menu_key


def create_main_menu_keyboard():
    """Создает клавиатуру для кнопки 'Главное меню'"""
    rows = [
        [InlineKeyboardButton(text="↩️Главное меню", callback_data="main_menu")],
    ]
    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_menu_key


def create_my_details_keyboard():
    """Создает клавиатуру для кнопки 'Мои данные'"""
    my_details_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Регистрация', callback_data='my_details')]
    ])

    return my_details_keyboard


def create_contact_keyboard():
    """Создает клавиатуру для отправки контакта"""
    rows = [
        [KeyboardButton(text="📱 Отправить", request_contact=True)]
    ]

    contact_keyboard = ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True, one_time_keyboard=True)
    return contact_keyboard


def create_data_modification_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру для изменения данных"""
    # data_modification_keyboard = InlineKeyboardMarkup()
    rows = [
        [InlineKeyboardButton(text="✏️Изменить Имя", callback_data="edit_name"),
         InlineKeyboardButton(text="✏️Изменить Фамилию", callback_data="edit_surname")],
        [InlineKeyboardButton(text="✏️Изменить Город", callback_data="edit_city"),
         InlineKeyboardButton(text="✏️Изменить Номер 📱 ", callback_data="edit_phone")],
        [InlineKeyboardButton(text="↩️ Вернуться в начальное меню", callback_data="disagree")]]

    data_modification_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return data_modification_keyboard


def create_sign_up_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру для кнопок 'Согласен' и 'Не согласен'"""
    # sign_up_keyboard = InlineKeyboardMarkup()
    rows = [
        [InlineKeyboardButton(text='👍 Согласен', callback_data='agree'),
         InlineKeyboardButton(text='👎 Не согласен', callback_data='disagree')]]

    sign_up_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return sign_up_keyboard


if __name__ == '__main__':
    create_packaging_menu_keyboard()
    create_packaging_keyboard()
    create_main_menu_keyboard()
    create_my_details_keyboard()
    create_contact_keyboard()
    create_data_modification_keyboard()
    create_sign_up_keyboard()
    create_services_and_prices_main_menu_keyboard()
    create_services_and_prices_keyboard()
    create_greeting_keyboard()
