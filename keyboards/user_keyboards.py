from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# def create_greeting_keyboard():
#     """Создаем клавиатуру для приветственного сообщения 👋"""
#     greeting_keyboard = InlineKeyboardMarkup()
#     ask_anonymous_question_button = InlineKeyboardButton(text='⭐️ Услуги и цены',
#                                                          callback_data='services_and_prices')
#     sign_up_button = InlineKeyboardButton(text='🗒 Бланк заказа',
#                                           callback_data='order_form')
#     contact_operator_button = InlineKeyboardButton(text='🛍 Самовыкуп',
#                                                    callback_data="self_redemption")
#     partnership_conditions_for_intermediaries_button = InlineKeyboardButton(
#         text='💰 Партнерские условия для посредников',
#         callback_data="partnership_conditions_for_intermediaries_button")
#     contacts_and_address_button = InlineKeyboardButton(text='📦 Виды упаковки',
#                                                        callback_data='types_of_packaging')
#     current_promotions_button = InlineKeyboardButton(text='💌 Отзывы',
#                                                      callback_data='reviews')
#     helpful_information_batton = InlineKeyboardButton(text='📚 Полезная информация', callback_data='useful_information')
#     leave_review_button = InlineKeyboardButton(text="📞 Связаться с менеджером",
#                                                callback_data='contact_the_manager')
#     greeting_keyboard.row(ask_anonymous_question_button)  # Услуги и цены
#     greeting_keyboard.row(sign_up_button, contact_operator_button)  # Самовыкуп
#     greeting_keyboard.row(partnership_conditions_for_intermediaries_button)  # Партнерские условия для посредников
#     greeting_keyboard.row(contacts_and_address_button,  # Виды упаковки
#                           current_promotions_button)  # Отзывы
#     greeting_keyboard.row(helpful_information_batton)  # Полезная информация
#     greeting_keyboard.row(leave_review_button)  # Связаться с менеджером
#
#     return greeting_keyboard

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
    greeting_keyboard.row(ask_anonymous_question_button, partnership_conditions_for_intermediaries_button)  # Услуги и цены
    greeting_keyboard.row(sign_up_button, contact_operator_button)  # Самовыкуп
    # greeting_keyboard.row(partnership_conditions_for_intermediaries_button)  # Партнерские условия для посредников
    greeting_keyboard.row(contacts_and_address_button,  # Виды упаковки
                          current_promotions_button)  # Отзывы
    greeting_keyboard.row(helpful_information_batton)  # Полезная информация
    greeting_keyboard.row(leave_review_button)  # Связаться с менеджером

    return greeting_keyboard

def create_greeting_keyboard_replyKeyboard():
    """Создаем клавиатуру для приветственного сообщения 👋"""
    greeting_keyboard_replyKeyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    ask_anonymous_question_button = KeyboardButton('⭐️ Услуги и цены')
    sign_up_button = KeyboardButton('🗒 Бланк заказа')
    contact_operator_button = KeyboardButton('🛍 Самовыкуп')
    partnership_conditions_for_intermediaries_button = KeyboardButton('💰 Партнерские условия для посредников')
    contacts_and_address_button = KeyboardButton('📦 Виды упаковки')
    current_promotions_button = KeyboardButton('💌 Отзывы')
    helpful_information_batton = KeyboardButton('📚 Полезная информация')
    update_the_bot_button = KeyboardButton('🔁 Обновить бота')
    leave_review_button = KeyboardButton("📞 Связаться с менеджером")
    greeting_keyboard_replyKeyboard.add(ask_anonymous_question_button)  # Услуги и цены
    greeting_keyboard_replyKeyboard.add(sign_up_button)  # Бланк заказа
    greeting_keyboard_replyKeyboard.add(contact_operator_button)  # Самовыкуп
    greeting_keyboard_replyKeyboard.add(
        partnership_conditions_for_intermediaries_button)  # Партнерские условия для посредников
    greeting_keyboard_replyKeyboard.add(contacts_and_address_button,  # Виды упаковки
                                        current_promotions_button)  # Отзывы
    greeting_keyboard_replyKeyboard.add(helpful_information_batton)  # Полезная информация
    greeting_keyboard_replyKeyboard.add(update_the_bot_button)  # Обновить бота
    greeting_keyboard_replyKeyboard.add(leave_review_button)  # Связаться с менеджером

    return greeting_keyboard_replyKeyboard


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
    button_10 = InlineKeyboardButton(text='Главное меню',
                                     callback_data='order_form')
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


if __name__ == '__main__':
    create_greeting_keyboard()
