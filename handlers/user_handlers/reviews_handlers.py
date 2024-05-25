# from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from loguru import logger

from system.dispatcher import router
from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from system.dispatcher import bot, dp


@router.callback_query(F.data == "reviews")
async def reviews(callback_query: types.CallbackQuery, state: FSMContext):
    """💌 Отзывы"""
    try:
        # await state.finish()  # Завершаем текущее состояние машины состояний
        # await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        await state.clear()  # Очищаем состояние
        greeting_message = (f'Вы можете посмотреть отзывы о нашей компании, а также все рабочие процессы!\n\n'

                            f'В нашем канале, он посвящен отзывам и рабочим процессам.\n'
                            f'<a href="https://t.me/cforb_review">• Перейти на канал</a>\n\n'

                            f'На специализированном  сайте "Отзовик"\n'
                            f'<a href="https://cforb.ru/obrazec-tovara-iz-kitaya">• Перейти на "Отзовик"</a>\n\n'

                            f'Связаться с менеджерами: @cargo_cfb')
        main_menu_keyboard = create_main_menu_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_keyboard,
                               parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_reviews_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(reviews)
