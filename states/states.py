from aiogram.fsm.state import StatesGroup, State


class MyStates(StatesGroup):
    """Отправка сообщений: текстовое сообщение, фото + текст"""
    waiting_for_message = State()
    waiting_for_image = State()
    waiting_for_caption = State()


class EditPaymentInfoStates(StatesGroup):
    edit_payment_text = State()


class FormeditWhatPaymentsAwaitMe(StatesGroup):
    text_edit_what_payments_await_me = State()


class FormeditPurchaseASupplierDatabase(StatesGroup):
    text_edit_purchase_a_supplier_database = State()


class FormeditWechatRegistrationService(StatesGroup):
    text_edit_wechat_registration_service = State()


class FormeditProductSearchService(StatesGroup):
    text_edit_product_search_service = State()


class FormeditGoodsRedemptionService(StatesGroup):
    text_edit_goods_redemption_service = State()


class FormeditCargoDeliveryPrices(StatesGroup):
    text_edit_cargo_delivery_prices = State()


class FileStates(StatesGroup):
    waiting_for_file = State()
    greeting_photo = State()  # Изменение фото в главном меню
    services_and_prices_photo = State()  # Изменение фото в разделе "Услуги и цены"
    white_cargo_gte_photo = State()  # Изменение фото в разделе "Белая доставка грузов с ГТД"
    types_of_packaging_photo = State()  # Изменение фото в разделе "Виды упаковки"


class FormeeditServicesAndPrices(StatesGroup):
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


class FormeditMainMenu(StatesGroup):
    """Замена текста в боте"""
    text_edit_main_menu = State()


class FormorderForm(StatesGroup):
    text_order_form = State()


class FormeditPartnershipConditionsIntermediariesButton(StatesGroup):
    text_edit_partnership_conditions_for_intermediaries_button = State()


class FormeditReviews(StatesGroup):
    text_edit_reviews = State()


class FormeditSelfRedemption(StatesGroup):
    text_edit_self_redemption = State()


class FormeeditTypesOfPackaging(StatesGroup):
    text_edit_types_of_packaging = State()


class FormeditBagTape(StatesGroup):
    text_edit_bag_tape = State()


class FormeeditBoxBagTape(StatesGroup):
    text_edit_box_bag_tape = State()


class FormeditWoodenSheathingBagTape(StatesGroup):
    text_edit_wooden_sheathing_bag_tape = State()


class FormeditWoodenCornersBagTape(StatesGroup):
    text_edit_wooden_corners_bag_tape = State()


class FormeditPalletCrate(StatesGroup):
    text_edit_pallet_crate = State()


class FormeditPalletWithASolidWoodenBox(StatesGroup):
    text_edit_pallet_with_a_solid_wooden_box = State()


class FormeditUsefulInformation(StatesGroup):
    text_edit_useful_information = State()


class EditWhiteCargoDeliveryState(StatesGroup):
    edit_text = State()
