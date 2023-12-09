from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards import keyboard_to_main_menu
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "partnership_conditions_for_intermediaries_button")
async def partnership_conditions_for_intermediaries(callback_query: types.CallbackQuery, state: FSMContext):
    """Партнерские условия для посредников"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"Приветствуем! 🌟 Если вы занимаетесь посредничеством с Китаем, доставкой грузов или "
                            f"управляете компанией, каналом, группой или курсами, приглашаем вас рассмотреть "
                            f"партнерство с нами. 🤝\n\n"
                            f"🌐 Почему с нами?\n\n"
                            f"- Индивидуальные условия для вас"
                            f"- Первоклассные цены и удобство работы"
                            f"- Обмен опытом и знаниями\n\n"
                            f"💼 Мы предлагаем гибкое сотрудничество по системе 'Промокод' или специальный прайс. "
                            f"Если вы верите своему китайскому партнеру на 100%, может быть, вы не знаете китайцев "
                            f"на 90%.\n\n"
                            f"🤝 <b>Свяжитесь с нами, обсудим варианты!</b>\n"
                            f"📩 Наша команда успешно сотрудничает с крупными российскими посредниками.\n\n"
                            f"🔗 Контакты: @cargo_cfb")
        main_menu_keyboard = keyboard_to_main_menu()
        with open('media/photos/partnership_conditions_for_intermediaries_button.jpg', 'rb') as photo_file:
            await bot.send_photo(callback_query.from_user.id,  # ID пользователя
                                 caption=greeting_message,  # Текст для приветствия 👋
                                 photo=photo_file,
                                 reply_markup=main_menu_keyboard,
                                 parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_partnership_conditions_for_intermediaries_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(partnership_conditions_for_intermediaries)
