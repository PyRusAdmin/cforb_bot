from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_greeting_keyboard():
    """Создает клавиатуру для приветственного сообщения 👋"""
    greeting_keyboard = InlineKeyboardMarkup()
    ask_anonymous_question_button = InlineKeyboardButton(text='🤔 Услуги и цены',
                                                         callback_data='services_and_prices')
    sign_up_button = InlineKeyboardButton(text='📝 Бланк заказа',
                                          callback_data='order_form')
    contacts_and_address_button = InlineKeyboardButton(text='📍 Виды упаковки',
                                                       callback_data='types_of_packaging')
    contact_operator_button = InlineKeyboardButton(text='👩‍💼 Самовыкуп',
                                                   callback_data="self_redemption")
    current_promotions_button = InlineKeyboardButton(text='🎁 Отзывы',
                                                     callback_data='reviews')
    leave_review_button = InlineKeyboardButton(text="📞 Связаться с менеджером",
                                               callback_data='contact_the_manager')

    greeting_keyboard.row(ask_anonymous_question_button)  # Задать анонимный вопрос
    greeting_keyboard.row(sign_up_button)  # Записаться
    greeting_keyboard.row(contacts_and_address_button,  # Контакты и адрес
                          current_promotions_button)  # Текущие акции
    greeting_keyboard.row(contact_operator_button)  # Связаться с оператором
    greeting_keyboard.row(leave_review_button)  # Оставить отзыв

    return greeting_keyboard


def services_and_prices_key():
    """Клавиатура услуг и цен"""
    services_and_prices_keyboard = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='Прайсы на доставку Карго',
                                    callback_data='cargo_delivery_prices')
    button_2 = InlineKeyboardButton(text='Белая доставка грузов с ГТД',
                                    callback_data='white_cargo_delivery_with_gas_turbine_engine')
    button_3 = InlineKeyboardButton(text='Услуга Выкупа товаров',
                                    callback_data='order_form')
    button_4 = InlineKeyboardButton(text='Услуга Поиска товаров (производителей в Китае)',
                                    callback_data='order_form')
    button_5 = InlineKeyboardButton(text='Инспекция поставщиков по провинциям (выезд на производство)',
                                    callback_data='order_form')
    button_6 = InlineKeyboardButton(text='Услуга регистрации WeChat',
                                    callback_data='order_form')
    button_7 = InlineKeyboardButton(text='Приобрести базу поставщиков',
                                    callback_data='order_form')
    button_8 = InlineKeyboardButton(text='Какие платежи меня ожидают?',
                                    callback_data='order_form')
    button_9 = InlineKeyboardButton(text='Как совершается оплата?',
                                    callback_data='order_form')
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
