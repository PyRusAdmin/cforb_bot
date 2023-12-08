from aiogram import executor
from loguru import logger

from handlers.greeting_handlers import register_greeting_handler
from handlers.order_form_handlers import register_order_form_handler
from handlers.partnership_conditions_for_intermediaries_handlers import \
    register_partnership_conditions_for_intermediaries_handler
from handlers.services_and_prices_handlers import register_services_and_prices_handler
from handlers.types_of_packaging_handlers import register_types_of_packaging_handler
from system.dispatcher import dp

logger.add("logs/log.log", retention="1 days", enqueue=True)  # Логирование бота


def main() -> None:
    """Запуск бота https://t.me/cforb_bot"""
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as error:
        logger.exception(error)
    register_greeting_handler()
    register_services_and_prices_handler()
    register_order_form_handler()  # Кнопка "Бланк заказа"
    register_types_of_packaging_handler()  # Кнопка "Виды упаковки"
    register_partnership_conditions_for_intermediaries_handler() # Партнерские условия для посредников


if __name__ == '__main__':
    try:
        main()  # Запуск бота
    except Exception as e:
        logger.exception(e)
