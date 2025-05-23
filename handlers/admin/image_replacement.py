import os

from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.states import (FileStates)
from system.dispatcher import ADMIN_USER_ID, router


@router.message(Command("greeting_photo"))
async def greeting_photo(message: types.Message, state: FSMContext):
    """Запрос нового фото для приветствия"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Пожалуйста, отправьте новое фото для замены в формате JPG.")
    await state.set_state(FileStates.greeting_photo)


@router.message(FileStates.greeting_photo)
async def replace_photo(message: types.Message, state: FSMContext):
    """Обработка присланного фото и замена файла"""
    if not message.photo:
        await message.answer("Пожалуйста, отправьте изображение.")
        return
    photo = message.photo[-1]
    file_info = await message.bot.get_file(photo.file_id)
    os.makedirs("media/photos/", exist_ok=True)  # Убедимся, что папка существует
    destination_path = os.path.join("media/photos/", 'greeting.jpg')
    await message.bot.download_file(file_info.file_path, destination_path)
    await message.answer("Фото успешно заменено!")
    await state.clear()


@router.message(Command("services_and_prices_photo"))
async def services_and_prices_photo(message: types.Message, state: FSMContext):
    """Запрос нового фото для Услуги и цены"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Пожалуйста, отправьте новое фото для замены в формате JPG.")
    await state.set_state(FileStates.services_and_prices_photo)


@router.message(FileStates.services_and_prices_photo)
async def replace_photo(message: types.Message, state: FSMContext):
    """Обработка присланного фото и замена файла Услуги и цены"""
    if not message.photo:
        await message.answer("Пожалуйста, отправьте изображение.")
        return
    photo = message.photo[-1]
    file_info = await message.bot.get_file(photo.file_id)
    os.makedirs("media/photos/", exist_ok=True)  # Убедимся, что папка существует
    destination_path = os.path.join("media/photos/", 'services_and_prices.jpg')
    await message.bot.download_file(file_info.file_path, destination_path)
    await message.answer("Фото успешно заменено!")
    await state.clear()


@router.message(Command("white_cargo_gte_photo"))
async def cmd_replace_white_cargo_photo(message: types.Message, state: FSMContext):
    """Запрос нового фото для Белой доставка грузов с ГТД"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Пожалуйста, отправьте новое фото для замены в формате JPG.")
    await state.set_state(FileStates.white_cargo_gte_photo)


@router.message(FileStates.white_cargo_gte_photo)
async def handle_photo_upload(message: types.Message, state: FSMContext):
    """Обработка присланного фото и замена файла Белая доставка грузов с ГТД"""
    if not message.photo:
        await message.answer("Пожалуйста, отправьте изображение.")
        return
    photo = message.photo[-1]
    file_info = await message.bot.get_file(photo.file_id)
    os.makedirs("media/photos/", exist_ok=True)  # Убедимся, что папка существует
    destination_path = os.path.join("media/photos/", 'white_cargo_gte.jpg')
    await message.bot.download_file(file_info.file_path, destination_path)
    await message.answer("Фото успешно заменено!")
    await state.clear()


@router.message(Command("types_of_packaging_photo"))
async def types_of_packaging_photo(message: types.Message, state: FSMContext):
    """Запрос нового фото для Виды упаковки"""
    if message.from_user.id not in ADMIN_USER_ID:
        await message.reply("У вас нет прав на выполнение этой команды.")
        return
    await message.answer("Пожалуйста, отправьте новое фото для замены в формате JPG.")
    await state.set_state(FileStates.white_cargo_gte_photo)


@router.message(FileStates.white_cargo_gte_photo)
async def replace_photo(message: types.Message, state: FSMContext):
    """Обработка присланного фото и замена файла Виды упаковки"""
    if not message.photo:
        await message.answer("Пожалуйста, отправьте изображение.")
        return
    photo = message.photo[-1]
    file_info = await message.bot.get_file(photo.file_id)
    os.makedirs("media/photos/", exist_ok=True)  # Убедимся, что папка существует
    destination_path = os.path.join("media/photos/", 'types_of_packaging.jpg')
    await message.bot.download_file(file_info.file_path, destination_path)
    await message.answer("Фото успешно заменено!")
    await state.clear()


def register_handlers_image_replacement():
    """Функция регистрации обработчиков для замены фото"""
    router.message.register(greeting_photo, Command("greeting_photo"))
    router.message.register(replace_photo, FileStates.greeting_photo)

    router.message.register(services_and_prices_photo, Command("services_and_prices_photo"))
    router.message.register(replace_photo, FileStates.services_and_prices_photo)

    router.message.register(cmd_replace_white_cargo_photo, Command("white_cargo_gte_photo"))
    router.message.register(handle_photo_upload, FileStates.white_cargo_gte_photo)

    router.message.register(types_of_packaging_photo, Command("types_of_packaging_photo"))
    router.message.register(replace_photo, FileStates.types_of_packaging_photo)
