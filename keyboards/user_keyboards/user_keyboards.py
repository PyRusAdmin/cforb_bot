from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def create_packaging_menu_keyboard():
    """
    Создает клавиатуру для выбора видов упаковки.
    Кнопка "Назад к упаковкам" возвращает к предыдущему меню ('types_of_packaging').
    Кнопка "Главное меню" возвращает к главному меню ('main_menu').
    """
    packaging_menu_keyboard = InlineKeyboardMarkup()
    back_button = InlineKeyboardButton(text='Назад к упаковкам',
                                       callback_data='types_of_packaging')
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')
    packaging_menu_keyboard.add(back_button)
    packaging_menu_keyboard.add(main_menu_button)
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
    packaging_keyboard = InlineKeyboardMarkup()
    button_bag_tape = InlineKeyboardButton(text='Мешок + скотч',
                                           callback_data='bag_tape')
    button_box_bag_tape = InlineKeyboardButton(text='Коробка + мешок + скотч',
                                               callback_data='box_bag_tape')
    button_wooden_sheathing_bag_tape = InlineKeyboardButton(text='Деревянная обрешетка + мешок + скотч',
                                                            callback_data='wooden_sheathing_bag_tape')
    button_wooden_corners_bag_tape = InlineKeyboardButton(text='Деревянные уголки + мешок + скотч',
                                                          callback_data='wooden_corners_bag_tape')
    button_pallet_in_crate = InlineKeyboardButton(text='Паллет в обрешетке',
                                                  callback_data='pallet_in_crate')
    button_pallet_with_solid_wooden_box = InlineKeyboardButton(text='Паллет с глухим деревянным коробом',
                                                               callback_data='pallet_with_a_solid_wooden_box')
    button_main_menu = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')
    packaging_keyboard.add(button_bag_tape)
    packaging_keyboard.add(button_box_bag_tape)
    packaging_keyboard.add(button_wooden_sheathing_bag_tape)
    packaging_keyboard.add(button_wooden_corners_bag_tape)
    packaging_keyboard.add(button_pallet_in_crate)
    packaging_keyboard.add(button_pallet_with_solid_wooden_box)
    packaging_keyboard.add(button_main_menu)
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
    greeting_keyboard = InlineKeyboardMarkup()
    ask_anonymous_question_button = InlineKeyboardButton(text='⭐️ Услуги и цены',
                                                         callback_data='services_and_prices')
    order_form_button = InlineKeyboardButton(text='🗒 Бланк заказа',
                                             callback_data='order_form')
    self_redemption_button = InlineKeyboardButton(text='🛍 Самовыкуп',
                                                  callback_data="self_redemption")
    partnership_button = InlineKeyboardButton(text='💰 Партнерка',
                                              callback_data="partnership_conditions_for_intermediaries_button")
    types_of_packaging_button = InlineKeyboardButton(text='📦 Виды упаковки',
                                                     callback_data='types_of_packaging')
    reviews_button = InlineKeyboardButton(text='💌 Отзывы',
                                          callback_data='reviews')
    useful_information_button = InlineKeyboardButton(text='📚 Полезная информация',
                                                     callback_data='useful_information')
    contact_manager_button = InlineKeyboardButton(text="📞 Связаться с менеджером",
                                                  url='https://t.me/cargo_cfb')
    greeting_keyboard.row(ask_anonymous_question_button,
                          partnership_button)  # Услуги и цены
    greeting_keyboard.row(order_form_button, self_redemption_button)  # Самовыкуп
    greeting_keyboard.row(types_of_packaging_button,  # Виды упаковки
                          reviews_button)  # Отзывы
    greeting_keyboard.row(useful_information_button)  # Полезная информация
    greeting_keyboard.row(contact_manager_button)  # Связаться с менеджером

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
    services_and_prices_keyboard = InlineKeyboardMarkup()

    cargo_delivery_prices_button = InlineKeyboardButton(text='Прайсы на доставку Карго',
                                                        callback_data='cargo_delivery_prices')
    white_cargo_delivery_button = InlineKeyboardButton(text='Белая доставка грузов с ГТД',
                                                       callback_data='white_cargo_delivery_with_gas_turbine_engine')
    goods_redemption_button = InlineKeyboardButton(text='Услуга Выкупа товаров',
                                                   callback_data='goods_redemption_service')
    product_search_button = InlineKeyboardButton(text='Услуга Поиска товаров (производителей в Китае)',
                                                 callback_data='product_search_service')
    supplier_inspection_button = InlineKeyboardButton(
        text='Инспекция поставщиков по провинциям (выезд на производство)',
        callback_data='supplier_inspection_by_province')
    wechat_registration_button = InlineKeyboardButton(text='Услуга регистрации WeChat',
                                                      callback_data='wechat_registration_service')
    purchase_supplier_database_button = InlineKeyboardButton(text='Приобрести базу поставщиков',
                                                             callback_data='purchase_a_supplier_database')
    expected_payments_button = InlineKeyboardButton(text='Какие платежи меня ожидают?',
                                                    callback_data='what_payments_await_me')
    payment_process_button = InlineKeyboardButton(text='Как совершается оплата?',
                                                  callback_data='how_is_payment_made')
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню',
                                            callback_data='main_menu')

    services_and_prices_keyboard.row(cargo_delivery_prices_button)
    services_and_prices_keyboard.row(white_cargo_delivery_button)
    services_and_prices_keyboard.row(goods_redemption_button)
    services_and_prices_keyboard.row(product_search_button)
    services_and_prices_keyboard.row(supplier_inspection_button)
    services_and_prices_keyboard.row(wechat_registration_button)
    services_and_prices_keyboard.row(purchase_supplier_database_button)
    services_and_prices_keyboard.row(expected_payments_button)
    services_and_prices_keyboard.row(payment_process_button)
    services_and_prices_keyboard.row(main_menu_button)

    return services_and_prices_keyboard


def create_services_and_prices_main_menu_keyboard():
    """Создает клавиатуру для кнопки 'Главное меню' из раздела 'Услуги и цены'"""
    services_and_prices_main_menu_keyboard = InlineKeyboardMarkup()

    back_to_services_button = InlineKeyboardButton(text='Назад к услугам', callback_data='services_and_prices')
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')

    services_and_prices_main_menu_keyboard.row(back_to_services_button)
    services_and_prices_main_menu_keyboard.row(main_menu_button)

    return services_and_prices_main_menu_keyboard


def create_main_menu_keyboard():
    """Создает клавиатуру для кнопки 'Главное меню'"""
    main_menu_keyboard = InlineKeyboardMarkup()
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')

    main_menu_keyboard.row(main_menu_button)
    return main_menu_keyboard


def create_my_details_keyboard():
    """Создает клавиатуру для кнопки 'Мои данные'"""
    my_details_keyboard = InlineKeyboardMarkup()

    registration_button = InlineKeyboardButton(text='Регистрация', callback_data='my_details')

    my_details_keyboard.row(registration_button)

    return my_details_keyboard


def create_contact_keyboard():
    """Создает клавиатуру для отправки контакта"""
    contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    send_contact_button = KeyboardButton("📱 Отправить", request_contact=True)

    contact_keyboard.add(send_contact_button)
    return contact_keyboard


def create_data_modification_keyboard():
    """Создает клавиатуру для изменения данных"""
    data_modification_keyboard = InlineKeyboardMarkup()
    edit_name_button = InlineKeyboardButton("✏️Изменить Имя", callback_data="edit_name")
    edit_surname_button = InlineKeyboardButton("✏️Изменить Фамилию", callback_data="edit_surname")
    edit_city_button = InlineKeyboardButton("✏️Изменить Город", callback_data="edit_city")
    edit_phone_button = InlineKeyboardButton("✏️Изменить Номер 📱 ", callback_data="edit_phone")
    start_button = InlineKeyboardButton("↩️ Вернуться в начальное меню", callback_data="disagree")

    data_modification_keyboard.row(edit_name_button, edit_surname_button)
    data_modification_keyboard.row(edit_city_button, edit_phone_button)
    data_modification_keyboard.row(start_button)
    return data_modification_keyboard


def create_sign_up_keyboard():
    """Создает клавиатуру для кнопок 'Согласен' и 'Не согласен'"""
    sign_up_keyboard = InlineKeyboardMarkup()
    agree_button = InlineKeyboardButton(text='👍 Согласен', callback_data='agree')
    disagree_button = InlineKeyboardButton(text='👎 Не согласен', callback_data='disagree')

    sign_up_keyboard.row(agree_button, disagree_button)
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
