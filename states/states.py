from aiogram.fsm.state import StatesGroup, State


class MyStates(StatesGroup):
    """Отправка сообщений: текстовое сообщение, фото + текст"""
    waiting_for_message = State()  # Состояние ожидания текста
    waiting_for_image = State()  # Состояние ожидания фото
    waiting_for_caption = State()  # Состояние ожидания текста


class FileStates(StatesGroup):
    waiting_for_file = State()
    greeting_photo = State()  # Изменение фото в главном меню
    services_and_prices_photo = State()  # Изменение фото в разделе "Услуги и цены"
    white_cargo_gte_photo = State()  # Изменение фото в разделе "Белая доставка грузов с ГТД"
    types_of_packaging_photo = State()  # Изменение фото в разделе "Виды упаковки"


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


class BotContentEditStates(StatesGroup):
    """Замена текста в боте"""
    edit_main_menu = State()  # Замена текста в главном меню
    edit_types_of_packaging = State()  # Замена текста в разделе "Виды упаковки"
    edit_services_and_prices = State()  # Замена текста в разделе "Услуги и цены"
    edit_wooden_corners_bag_tape = State()  # Замена текста в разделе "Деревянные уголки + мешок + скотч"
    edit_wooden_sheathing_bag_tape = State()  # Замена текста в разделе "Деревянная обрешетка + мешок + скотч"
    order_form = State()  # Замена текста в разделе "🗒 Бланк заказа"
    edit_bag_tape = State()  # Замена текста в разделе "Мешок + скотч"
    edit_box_bag_tape = State()  # Замена текста в разделе "Коробка + мешок + скотч"
    edit_pallet_crate = State()  # Замена текста в разделе "Паллет в обрешетке"
    edit_pallet_with_a_solid_wooden_box = State()  # Замена текста в разделе "Паллет с глухим деревянным коробом"
    edit_cargo_delivery_prices = State()  # Замена текста в разделе "Прайсы на доставку Карго"
    edit_goods_redemption_service = State()  # Замена текста в разделе "Услуга Выкупа товаров"
    edit_product_search_service = State()  # Замена текста в разделе "Услуга Поиска товаров (производителей в Китае)"
    edit_text = State()  # Замена текста в разделе "Инспекция поставщиков по провинциям (выезд на производство)
    edit_wechat_registration_service = State()  # Замена текста в разделе "Услуга регистрации в WeChat"
    edit_purchase_a_supplier_database = State()  # Замена текста в разделе "Приобрести базу данных поставщиков"
    edit_what_payments_await_me = State()  # Замена текста в разделе "Какие платежи меня ожидают?"
    edit_payment_text = State()  # Замена текста в разделе "Как совершается оплата?"
    edit_self_redemption = State()  # Замена текста в разделе "🛍 Самовыкуп"
    edit_reviews = State()  # Замена текста в разделе "💌 Отзывы"
    edit_partnership_conditions_for_intermediaries_button = State()  # Замена текста в разделе "Партнерские условия для посредников"
    edit_text_white_cargo_gte = State()  # Замена текста в разделе "Белая доставка грузов с ГТД"
    text_edit_useful_information = State()  # Замена текста в разделе "📚 Полезная информация"
