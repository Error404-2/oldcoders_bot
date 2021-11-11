from aiogram import types
from aiogram.dispatcher.webhook import SendMessage
from dispatcher import dp
import config


@dp.message_handler()
async def echo(message: types.Message):

    match message.text.lower():
        case "/инфо" | "/info":
            await message.answer("https://github.com/OldCodersClub/faq")
        case "/secret":
            await SendMessage(message.chat.id, message.text)

    if "привет деды" in message.text.lower():
        await message.answer("И тобе привет Cтарина")
    elif "вступил(а) в группу" in message.text.lower():
        await message.answer("Добро пожаловать\nСоветуем ознакомиться с дедовским архивом знаний\n\n\nhttps://github.com/OldCodersClub/faq")


# @dp.message_handler(text=["/инфо", "/info"])
# async def text_in_handler(message: types.Message):
#     await message.answer("https://github.com/OldCodersClub/faq")