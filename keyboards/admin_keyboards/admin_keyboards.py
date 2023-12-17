from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_create_greeting_keyboard():
    """Создаем клавиатуру для приветственного сообщения 👋 для админов"""
    greeting_keyboard = InlineKeyboardMarkup()
    users_who_launched_button = InlineKeyboardButton(text='Получить пользователей запустивших бота',
                                                     callback_data='get_users_who_launched_the_bot')
    list_of_registered_users_button = InlineKeyboardButton(
        text='Получить список зарегистрированных пользователей',
        callback_data='get_a_list_of_users_registered_in_the_bot')
    send_message_button = InlineKeyboardButton(text='Отправить сообщение пользователям бота',
                                               callback_data="send_a_message_to_bot_users")
    send_image_button = InlineKeyboardButton(text='Отправить изображение пользователям бота',
                                             callback_data="send_an_image_to_bot_users")

    greeting_keyboard.row(users_who_launched_button)  # Получить пользователей запустивших бота
    greeting_keyboard.row(list_of_registered_users_button)  # Получить список пользователей зарегистрировавшихся в боте
    greeting_keyboard.row(send_message_button)  # Отправить сообщение пользователям бота
    greeting_keyboard.row(send_image_button)

    return greeting_keyboard


if __name__ == '__main__':
    admin_create_greeting_keyboard()
