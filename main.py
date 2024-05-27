import asyncio
import logging
import sys

from loguru import logger

from handlers.admin_handlers.admin_greeting_handlers import register_admin_greeting_handler
from handlers.services_prices_handlers.how_is_payment_made_handlers import register_how_is_payment_made
from handlers.services_prices_handlers.supplier_inspection_handlers import \
    register_handle_supplier_inspection
from handlers.services_prices_handlers.white_cargo_callback_handler import \
    register_handle_white_cargo_callback
from handlers.user_handlers.greeting_handlers import register_greeting_handler
from handlers.user_handlers.order_form_handlers import register_order_form_handler
from handlers.user_handlers.partnership_conditions_for_intermediaries_handlers import \
    register_partnership_conditions_for_intermediaries_handler
from handlers.user_handlers.reviews_handlers import register_reviews_handler
from handlers.user_handlers.self_redemption_handlers import register_self_redemption_handler
from handlers.services_prices_handlers.services_and_prices_handlers import register_services_and_prices_handler
from handlers.user_handlers.types_of_packaging_handlers import register_types_of_packaging_handler
from handlers.user_handlers.useful_information_handlers import register_useful_information_handler
from system.dispatcher import dp, bot

logger.add("logs/log.log", retention="1 days", enqueue=True)  # Логирование бота


async def main() -> None:
    """Запуск бота https://t.me/cforb_bot"""
    await dp.start_polling(bot)
    register_greeting_handler()

    register_services_and_prices_handler()  # Услуги и цены
    register_how_is_payment_made()  # Как совершается оплата?
    register_handle_white_cargo_callback() # Белая доставка грузов с ГТД
    register_handle_supplier_inspection() # Информация о посредниках

    register_order_form_handler()  # 🗒 Бланк заказа
    register_types_of_packaging_handler()  # 📦 Виды упаковки
    register_partnership_conditions_for_intermediaries_handler()  # Партнерские условия для посредников
    register_self_redemption_handler()  # Самовыкуп
    register_reviews_handler()  # 💌 Отзывы
    register_useful_information_handler()  # 📚 Полезная информация
    register_admin_greeting_handler()  # Стартовая админ панель


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
