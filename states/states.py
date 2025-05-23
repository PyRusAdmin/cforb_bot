from aiogram.fsm.state import StatesGroup, State


class MyStates(StatesGroup):
    """Отправка сообщений: текстовое сообщение, фото + текст"""
    waiting_for_message = State()
    waiting_for_image = State()
    waiting_for_caption = State()

class EditPaymentInfoStates(StatesGroup):
    edit_payment_text = State()


class Formedit_what_payments_await_me(StatesGroup):
    text_edit_what_payments_await_me = State()

class Formedit_purchase_a_supplier_database(StatesGroup):
    text_edit_purchase_a_supplier_database = State()


class Formedit_wechat_registration_service(StatesGroup):
    text_edit_wechat_registration_service = State()


class Formedit_product_search_service(StatesGroup):
    text_edit_product_search_service = State()


class Formedit_goods_redemption_service(StatesGroup):
    text_edit_goods_redemption_service = State()

class Formedit_cargo_delivery_prices(StatesGroup):
    text_edit_cargo_delivery_prices = State()

class FileStates(StatesGroup):
    waiting_for_file = State()

class Formeedit_services_and_prices(StatesGroup):
    text_edit_services_and_prices = State()

class EditSupplierInspectionState(StatesGroup):
    edit_text = State()

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

class Formedit_main_menu(StatesGroup):
    text_edit_main_menu = State()

class Formorder_form(StatesGroup):
    text_order_form = State()


class FormeditPartnershipConditionsIntermediariesButton(StatesGroup):
    text_edit_partnership_conditions_for_intermediaries_button = State()

class Formedit_reviews(StatesGroup):
    text_edit_reviews = State()

class Formedit_self_redemption(StatesGroup):
    text_edit_self_redemption = State()

class Formeedit_types_of_packaging(StatesGroup):
    text_edit_types_of_packaging = State()

class Formedit_bag_tape(StatesGroup):
    text_edit_bag_tape = State()

class Formeedit_box_bag_tape(StatesGroup):
    text_edit_box_bag_tape = State()

class Formedit_wooden_sheathing_bag_tape(StatesGroup):
    text_edit_wooden_sheathing_bag_tape = State()

class Formedit_wooden_corners_bag_tape(StatesGroup):
    text_edit_wooden_corners_bag_tape = State()

class Formedit_pallet_crate(StatesGroup):
    text_edit_pallet_crate = State()

class Formedit_pallet_with_a_solid_wooden_box(StatesGroup):
    text_edit_pallet_with_a_solid_wooden_box = State()

class Formedit_useful_information(StatesGroup):
    text_edit_useful_information = State()