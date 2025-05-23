import asyncio
import logging
import sys

from loguru import logger

from handlers.admin.admin_greeting import register_admin_greeting_handler
from handlers.admin.sending_messages import register_handlers_sending_messages
from handlers.services_prices.how_is_payment_made import register_how_is_payment_made
from handlers.services_prices.supplier_inspection import register_handle_supplier_inspection
from handlers.services_prices.white_cargo_callback import register_handle_white_cargo_callback
from handlers.user.greeting import register_greeting_handler
from handlers.user.order_form import register_order_form_handler
from handlers.user.partnership_conditions_intermediaries import register_partnership_conditions_intermediaries_handler
from handlers.user.reviews import register_reviews_handler
from handlers.user.self_redemption import register_self_redemption_handler
from handlers.services_prices.services_and_prices import register_services_and_prices_handler
from handlers.user.types_of_packaging import register_types_of_packaging_handler
from handlers.user.useful_information import register_useful_information_handler
from system.dispatcher import dp, bot

logger.add("logs/log.log", retention="1 days", enqueue=True)  # Логирование бота


async def main() -> None:
    """Запуск бота https://t.me/cforb_bot"""
    await dp.start_polling(bot)
    register_greeting_handler()

    register_services_and_prices_handler()  # Услуги и цены
    register_how_is_payment_made()  # Как совершается оплата?
    register_handle_white_cargo_callback()  # Белая доставка грузов с ГТД
    register_handle_supplier_inspection()  # Информация о посредниках

    register_order_form_handler()  # 🗒 Бланк заказа
    register_types_of_packaging_handler()  # 📦 Виды упаковки
    register_partnership_conditions_intermediaries_handler()  # Партнерские условия для посредников
    register_self_redemption_handler()  # Самовыкуп
    register_reviews_handler()  # 💌 Отзывы
    register_useful_information_handler()  # 📚 Полезная информация
    register_admin_greeting_handler()  # Стартовая админ панель

    register_handlers_sending_messages() # Отправка сообщений, пользователям бота

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
