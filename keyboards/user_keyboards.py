from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def create_greeting_keyboard():
    """Создаем клавиатуру для приветственного сообщения 👋"""
    greeting_keyboard = InlineKeyboardMarkup()
    ask_anonymous_question_button = InlineKeyboardButton(text='⭐️ Услуги и цены',
                                                         callback_data='services_and_prices')
    sign_up_button = InlineKeyboardButton(text='🗒 Бланк заказа',
                                          callback_data='order_form')
    contact_operator_button = InlineKeyboardButton(text='🛍 Самовыкуп',
                                                   callback_data="self_redemption")
    partnership_conditions_for_intermediaries_button = InlineKeyboardButton(
        text='💰 Партнерка',
        callback_data="partnership_conditions_for_intermediaries_button")
    contacts_and_address_button = InlineKeyboardButton(text='📦 Виды упаковки',
                                                       callback_data='types_of_packaging')
    current_promotions_button = InlineKeyboardButton(text='💌 Отзывы',
                                                     callback_data='reviews')
    helpful_information_batton = InlineKeyboardButton(text='📚 Полезная информация', callback_data='useful_information')
    leave_review_button = InlineKeyboardButton(text="📞 Связаться с менеджером",
                                               callback_data='contact_the_manager')
    greeting_keyboard.row(ask_anonymous_question_button,
                          partnership_conditions_for_intermediaries_button)  # Услуги и цены
    greeting_keyboard.row(sign_up_button, contact_operator_button)  # Самовыкуп
    greeting_keyboard.row(contacts_and_address_button,  # Виды упаковки
                          current_promotions_button)  # Отзывы
    greeting_keyboard.row(helpful_information_batton)  # Полезная информация
    greeting_keyboard.row(leave_review_button)  # Связаться с менеджером

    return greeting_keyboard


def services_and_prices_key():
    """Клавиатура услуг и цен"""
    services_and_prices_keyboard = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='Прайсы на доставку Карго',
                                    callback_data='cargo_delivery_prices')
    button_2 = InlineKeyboardButton(text='Белая доставка грузов с ГТД',
                                    callback_data='white_cargo_delivery_with_gas_turbine_engine')
    button_3 = InlineKeyboardButton(text='Услуга Выкупа товаров',
                                    callback_data='goods_redemption_service')  #
    button_4 = InlineKeyboardButton(text='Услуга Поиска товаров (производителей в Китае)',
                                    callback_data='product_search_service')
    button_5 = InlineKeyboardButton(text='Инспекция поставщиков по провинциям (выезд на производство)',
                                    callback_data='supplier_inspection_by_province')
    button_6 = InlineKeyboardButton(text='Услуга регистрации WeChat',
                                    callback_data='wechat_registration_service')
    button_7 = InlineKeyboardButton(text='Приобрести базу поставщиков',
                                    callback_data='purchase_a_supplier_database')
    button_8 = InlineKeyboardButton(text='Какие платежи меня ожидают?',
                                    callback_data='what_payments_await_me')
    button_9 = InlineKeyboardButton(text='Как совершается оплата?',
                                    callback_data='how_is_payment_made')
    button_10 = InlineKeyboardButton(text='↩️ Главное меню',
                                     callback_data='main_menu')
    services_and_prices_keyboard.row(button_1)
    services_and_prices_keyboard.row(button_2)
    services_and_prices_keyboard.row(button_3)
    services_and_prices_keyboard.row(button_4)
    services_and_prices_keyboard.row(button_5)
    services_and_prices_keyboard.row(button_6)
    services_and_prices_keyboard.row(button_7)
    services_and_prices_keyboard.row(button_8)
    services_and_prices_keyboard.row(button_9)
    services_and_prices_keyboard.row(button_10)
    return services_and_prices_keyboard


def keyboard_to_main_menu():
    """Создает клавиатуру для кнопки 'Главное меню'"""
    main_menu_keyboard = InlineKeyboardMarkup()
    main_menu_button = InlineKeyboardButton(text='↩️ Главное меню', callback_data='main_menu')

    main_menu_keyboard.row(main_menu_button)
    return main_menu_keyboard


def create_my_details_keyboard():
    """Создает клавиатуру для кнопки 'Мои данные'"""
    my_details_keyboard = InlineKeyboardMarkup()
    my_details_button = InlineKeyboardButton(text='Регистрация', callback_data='my_details')

    my_details_keyboard.row(my_details_button)  # Связаться с оператором
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
    create_greeting_keyboard()
