from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from states.states import FormorderForm
from system.dispatcher import bot, ADMIN_USER_ID
from system.dispatcher import dp
from system.dispatcher import router
from system.working_with_files import load_bot_info, save_bot_info


@router.callback_query(F.data == "order_form")
async def order_form(callback_query: types.CallbackQuery, state: FSMContext):
    """Бланк заказа"""
    try:
        await state.clear()  # Очищаем состояние
        data = load_bot_info(messages="media/messages/order_form.json")
        document = FSInputFile('media/document/Бланк Заказа CFORB.xls')
        await bot.send_document(chat_id=callback_query.message.chat.id, document=document,
                                reply_markup=create_main_menu_keyboard(),
                                caption=data,
                                parse_mode="HTML")
    except Exception as error:
        logger.exception(error)


# Обработчик команды /edit_order_form (только для админа)
@router.message(Command("edit_order_form"))
async def edit_order_form(message: Message, state: FSMContext):
    """Редактирование: Бланк заказа"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Введите новый текст, используя разметку HTML.")
    await state.set_state(FormorderForm.text_order_form)


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormorderForm.text_order_form)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='media/messages/order_form.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_order_form_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(order_form)
    dp.message.register(edit_order_form)
