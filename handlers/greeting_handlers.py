from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ParseMode
from loguru import logger

from database.database import recording_data_of_users_who_launched_the_bot, get_user_data_from_db, \
    insert_user_data_to_database, update_phone_in_db, update_city_in_db, update_surname_in_db, update_name_in_db, \
    check_user_exists_in_db
from keyboards.user_keyboards import create_greeting_keyboard, create_contact_keyboard, create_my_details_keyboard, \
    create_data_modification_keyboard, create_sign_up_keyboard
from system.dispatcher import bot, dp


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию

    # Получаем информацию о пользователе
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    join_date = message.date.strftime("%Y-%m-%d %H:%M:%S")

    logger.info(f"Пользователь {username} ({user_id}) запустил бота в {join_date}")
    # Записываем информацию о пользователе в базу данных
    recording_data_of_users_who_launched_the_bot(user_id, username, first_name, last_name, join_date)

    user_exists = check_user_exists_in_db(user_id)  # Проверяем наличие пользователя в базе данных
    if user_exists:
        greeting_keyboard = create_greeting_keyboard()
        with open("media/photos/greeting.jpg", "rb") as photo_file:  # Загружаем фото для поста
            data = (f"<b>{first_name} {last_name}, спасибо что подписались на нашего бота!</b>\n\n"
                    "<b>🇨🇳 Компания CFB - предлагает широкий спектр услуг по бизнесу с Китаем!</b>\n\n"
                    "• С полным списком услуг Вы можете ознакомиться в меню бота.\n\n"
                    "Обязательно включите уведомления и не удаляйте этого бота из своих чатов!\n\n"
                    "• У Вас появится возможность мгновенно и автоматически получать актуальные прайс-листы, необходимую информацию по обновлениям и т.д.\n\n"
                    "<i>Сайт: www.cforb.ru</i>\n"
                    "<i>Telegram: https://t.me/cforb_tg</i>\n"
                    "<i>Вконтакте: https://vk.com/cforb</i>\n"
                    "<i>Instagram: https://www.instagram.com/cforb_in</i>\n"
                    "<i>YouTube: https://www.youtube.com/@cforb_tube</i>")
            await bot.send_photo(message.from_user.id, caption=data, photo=photo_file,
                                 reply_markup=greeting_keyboard, parse_mode=ParseMode.HTML)
    else:
        # Если пользователя нет в базе данных, предлагаем пройти регистрацию
        sign_up_text = ("⚠️ <b>Вы не зарегистрированы в нашей системе</b> ⚠️\n\n"
                        "Для доступа к этому разделу, пожалуйста, <b>зарегистрируйтесь</b>.\n\n"
                        "Для перехода в начальное меню нажмите /start")

        # Создаем клавиатуру с помощью my_details() (предполагается, что она существует)
        my_details_key = create_my_details_keyboard()
        # Отправляем сообщение с предложением зарегистрироваться и клавиатурой
        await bot.send_message(message.from_user.id, sign_up_text,
                               reply_markup=my_details_key,
                               parse_mode=ParseMode.HTML,
                               disable_web_page_preview=True)

@dp.callback_query_handler(lambda c: c.data == "main_menu")
async def send_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия 👋"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию

        # Получаем информацию о пользователе
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name

        logger.info(f"Пользователь {username} ({user_id}) вернулся в начальное меню")

        user_exists = check_user_exists_in_db(user_id)  # Проверяем наличие пользователя в базе данных
        if user_exists:
            greeting_keyboard = create_greeting_keyboard()
            with open("media/photos/greeting.jpg", "rb") as photo_file:  # Загружаем фото для поста
                data = (f"<b>{first_name} {last_name}, спасибо что подписались на нашего бота!</b>\n\n"
                        "<b>🇨🇳 Компания CFB - предлагает широкий спектр услуг по бизнесу с Китаем!</b>\n\n"
                        "• С полным списком услуг Вы можете ознакомиться в меню бота.\n\n"
                        "Обязательно включите уведомления и не удаляйте этого бота из своих чатов!\n\n"
                        "• У Вас появится возможность мгновенно и автоматически получать актуальные прайс-листы, "
                        "необходимую информацию по обновлениям и т.д.\n\n"
                        "<i>Сайт: www.cforb.ru</i>\n"
                        "<i>Telegram: https://t.me/cforb_tg</i>\n"
                        "<i>Вконтакте: https://vk.com/cforb</i>\n"
                        "<i>Instagram: https://www.instagram.com/cforb_in</i>\n"
                        "<i>YouTube: https://www.youtube.com/@cforb_tube</i>")
                await bot.send_photo(message.from_user.id, caption=data, photo=photo_file,
                                     reply_markup=greeting_keyboard, parse_mode=ParseMode.HTML)
        else:
            # Если пользователя нет в базе данных, предлагаем пройти регистрацию
            sign_up_text = ("⚠️ <b>Вы не зарегистрированы в нашей системе</b> ⚠️\n\n"
                            "Для доступа к этому разделу, пожалуйста, <b>зарегистрируйтесь</b>.\n\n"
                            "Для перехода в начальное меню нажмите /start")

            # Создаем клавиатуру с помощью my_details() (предполагается, что она существует)
            my_details_key = create_my_details_keyboard()
            # Отправляем сообщение с предложением зарегистрироваться и клавиатурой
            await bot.send_message(message.from_user.id, sign_up_text,
                                   reply_markup=my_details_key,
                                   parse_mode=ParseMode.HTML,
                                   disable_web_page_preview=True)
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "my_details")
async def call_us_handler(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id  # Получаем ID текущего пользователя
    user_data = get_user_data_from_db(user_id)  # Функция, которая получает данные о пользователе из базы данных

    if user_data:
        # Если данные о пользователе найдены в базе данных, отобразите их
        name = user_data.get('name', 'не указано')
        surname = user_data.get('surname', 'не указано')
        city = user_data.get('city', 'не указано')
        phone_number = user_data.get('phone_number', 'не указано')
        registration_date = user_data.get('registration_date')

        text_mes = (f"🤝 Добро пожаловать, {name} {surname}!\n"
                    "Ваши данные:\n\n"
                    f"✅ <b>Имя:</b> {name}\n"
                    f"✅ <b>Фамилия:</b> {surname}\n"
                    f"✅ <b>Город:</b> {city}\n"
                    f"✅ <b>Номер телефона:</b> {phone_number}\n"
                    f"✅ <b>Дата регистрации:</b> {registration_date}\n\n")
        edit_data_keyboard = create_data_modification_keyboard()
        await bot.send_message(callback_query.from_user.id, text_mes,
                               reply_markup=edit_data_keyboard,
                               parse_mode=ParseMode.HTML)
    else:
        # Если данные о пользователе не найдены, предложите пройти регистрацию
        keyboards_sign_up = create_sign_up_keyboard()
        sign_up_text = ("👋 Предлагаем нам с Вами познакомиться!\n\n"
                        "Информация о Ваших Ф.И.О., городе и номере телефона нужны для оптимизации и персонализации "
                        "работы нашего бота под наших клиентов.\n\n"
                        "Для возврата нажмите /start")
        await bot.send_message(callback_query.from_user.id, sign_up_text,
                               reply_markup=keyboards_sign_up,
                               parse_mode=ParseMode.HTML,
                               disable_web_page_preview=True)


class MakingAnOrder(StatesGroup):
    """Создание класса состояний"""
    write_name = State()  # Имя
    write_surname = State()  # Фамилия
    phone_input = State()  # Передача номера телефона кнопкой
    write_city = State()  # Запись города


class ChangingData(StatesGroup):
    """Создание класса состояний, для смены данных пользователем"""
    changing_name = State()  # Имя
    changing_surname = State()  # Фамилия
    changing_phone = State()  # Передача номера телефона кнопкой
    changing_city = State()  # Запись города


@dp.callback_query_handler(lambda c: c.data == "edit_name")
async def edit_name_handler(callback_query: types.CallbackQuery):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новое имя:")
    await ChangingData.changing_name.set()


@dp.message_handler(state=ChangingData.changing_name)
async def process_entered_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = message.from_user.id
        new_name = message.text
        if update_name_in_db(user_id, new_name):
            text_name = f"✅ Имя успешно изменено на {new_name} ✅\n\n" \
                        "Для возврата нажмите /start"
            await bot.send_message(user_id, text_name)
        else:
            text_name = "❌ Произошла ошибка при изменении имени ❌\n\n" \
                        "Для возврата нажмите /start"
            await bot.send_message(user_id, text_name)
        # Завершаем состояние после изменения имени
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == "edit_surname")
async def edit_surname_handler(callback_query: types.CallbackQuery):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новую фамилию:")
    await ChangingData.changing_surname.set()


@dp.message_handler(state=ChangingData.changing_surname)
async def process_entered_edit_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = message.from_user.id
        new_surname = message.text
        if update_surname_in_db(user_id, new_surname):
            text_surname = f"✅ Фамилия успешно изменена на {new_surname} ✅\n\n" \
                           "Для возврата нажмите /start"
            await bot.send_message(user_id, text_surname)
        else:
            text_surname = "❌ Произошла ошибка при изменении фамилии ❌\n\n" \
                           "Для возврата нажмите /start"
            await bot.send_message(user_id, text_surname)
        # Завершаем состояние после изменения имени
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == "edit_city")
async def edit_city_handler(callback_query: types.CallbackQuery):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новый город:")
    await ChangingData.changing_city.set()


@dp.message_handler(state=ChangingData.changing_city)
async def process_entered_edit_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = message.from_user.id
        new_city = message.text
        if update_city_in_db(user_id, new_city):
            text_city = f"✅ Город успешно изменен на {new_city} ✅\n\n" \
                        "Для возврата нажмите /start"
            await bot.send_message(user_id, text_city)
        else:
            text_city = "❌ Произошла ошибка при изменении города ❌\n\n" \
                        "Для возврата нажмите /start"
            await bot.send_message(user_id, text_city)
        # Завершаем состояние после изменения имени
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == "edit_phone")
async def edit_city_handler(callback_query: types.CallbackQuery):
    # Отправляем сообщение с запросом на ввод нового имени и включаем состояние
    await bot.send_message(callback_query.from_user.id, "Введите новый номер телефона:")
    await ChangingData.changing_phone.set()


@dp.message_handler(state=ChangingData.changing_phone)
async def process_entered_edit_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = message.from_user.id
        new_phone = message.text
        if update_phone_in_db(user_id, new_phone):
            text_phone = f"✅ Номер телефона успешно изменен на {new_phone} ✅\n\n" \
                         "Для возврата нажмите /start"
            await bot.send_message(user_id, text_phone)
        else:
            text_phone = "❌ Произошла ошибка при изменении номера телефона ❌\n\n" \
                         "Для возврата нажмите /start"
            await bot.send_message(user_id, text_phone)
        # Завершаем состояние после изменения имени
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == "agree")
async def agree_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await MakingAnOrder.write_surname.set()
    text_mes = ("👥 Введите вашу фамилию (желательно кириллицей):\n"
                "Пример: Петров, Иванова, Сидоренко")
    await bot.send_message(callback_query.from_user.id, text_mes)


@dp.message_handler(state=MakingAnOrder.write_surname)
async def write_surname_handler(message: types.Message, state: FSMContext):
    surname = message.text
    await state.update_data(surname=surname)
    await MakingAnOrder.write_name.set()
    text_mes = ("👤 Введите ваше имя (желательно кириллицей):\n"
                "Пример: Иван, Ольга, Анастасия")
    await bot.send_message(message.from_user.id, text_mes)


@dp.message_handler(state=MakingAnOrder.write_name)
async def write_city_handlers(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await MakingAnOrder.write_city.set()
    text_mes = ("🏙️ Введите ваш город (желательно кириллицей):\n"
                "Пример: Москва, Санкт-Петербург")
    await bot.send_message(message.from_user.id, text_mes)


@dp.message_handler(state=MakingAnOrder.write_city)
async def write_name_handler(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)
    sign_up_texts = (
        "Для ввода номера телефона вы можете поделиться номером телефона, нажав на кнопку или ввести его вручную.\n\n"
        "Чтобы ввести номер вручную, просто отправьте его в текстовом поле.")
    contact_keyboard = create_contact_keyboard()
    await bot.send_message(message.from_user.id, sign_up_texts,
                           reply_markup=contact_keyboard,  # Set the custom keyboard
                           parse_mode=types.ParseMode.HTML,
                           disable_web_page_preview=True)
    await MakingAnOrder.phone_input.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=MakingAnOrder.phone_input)
async def handle_contact(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    await handle_confirmation(message, state)


@dp.message_handler(lambda message: message.text and not message.contact, state=MakingAnOrder.phone_input)
async def handle_phone_text(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    await handle_confirmation(message, state)


async def handle_confirmation(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardRemove(selective=False)  # Remove the keyboard
    await message.answer("Спасибо за предоставленные данные.", reply_markup=markup)
    # Извлечение пользовательских данных из состояния
    user_data = await state.get_data()
    surname = user_data.get('surname', 'не указан')
    name = user_data.get('name', 'не указан')
    phone_number = user_data.get('phone_number', 'не указан')
    city = user_data.get('city', 'не указан')
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Получение ID аккаунта Telegram
    user_id = message.from_user.id
    # Составьте подтверждающее сообщение
    text_mes = (f"🤝 Рады познакомиться {name} {surname}! 🤝\n"
                "Ваши регистрационные данные:\n\n"
                f"✅ <b>Ваше Имя:</b> {name}\n"
                f"✅ <b>Ваша Фамилия:</b> {surname}\n"
                f"✅ <b>Ваш Город:</b> {city}\n"
                f"✅ <b>Ваш номер телефона:</b> {phone_number}\n"
                f"✅ <b>Ваша Дата регистрации:</b> {registration_date}\n\n"
                "Вы можете изменить свои данные в меню \"Мои данные\".\n\n"
                "Для возврата нажмите /start")
    insert_user_data_to_database(user_id, name, surname, city, phone_number, registration_date)
    await state.finish()  # Завершаем текущее состояние машины состояний
    await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
    # Создаем клавиатуру с помощью my_details() (предполагается, что она существует)
    await bot.send_message(message.from_user.id, text_mes)


def register_greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(send_start)  # Обработчик команды /start, он же пост приветствия 👋
