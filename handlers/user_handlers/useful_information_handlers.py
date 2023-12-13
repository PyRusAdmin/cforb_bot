from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards.user_keyboards import keyboard_to_main_menu
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "useful_information")
async def useful_information(callback_query: types.CallbackQuery, state: FSMContext):
    """📚 Полезная информация"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f'<b>Специально для Вас, наша компанию подготовила статьи с полезной информацией, это '
                            f'облегчит наше сотрудничество, и поможет вам разобраться в некоторых вопросах!\n\n</b>'

                            f'<a href="https://cforb.ru/kak-prinimat-gruz-iz-kitaya">Правила приемки груза из Китая '
                            f'в России</a>\n'
                            f'<a href="https://cforb.ru/put-tovara-iz-kitaya">Путь товара из Китая в Россию</a>\n'
                            f'<a href="https://cforb.ru/samovykup-information">Информация для самовыкупов товара</a>\n'
                            f'<a href="https://cforb.ru/vykup-v-kitae-information">Информация если Выкуп делаем Мы</a>\n'
                            f'<a href="https://cforb.ru/poisk-tovara-v-kitae-samomu">Самостоятельный поиск товара. '
                            f'Преимущества</a>\n'
                            f'<a href="https://cforb.ru/pretenzii-po-rabote">Претензии по работе</a>\n'
                            f'<a href="https://cforb.ru/vybor-tovara-v-kitae">Выбор товара: как не ошибиться</a>\n'
                            f'<a href="https://cforb.ru/documenty-na-tovar">Документы на товар</a>\n'
                            f'<a href="https://cforb.ru/obrazec-tovara-iz-kitaya">Образцы: заказ и проверка</a>\n')
        main_menu_keyboard = keyboard_to_main_menu()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_useful_information_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(useful_information)
