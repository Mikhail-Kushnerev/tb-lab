from aiogram import types
from aiogram.utils.callback_data import CallbackData


show_domen = CallbackData("info", "show", "name")


async def check_info(url):
    markup = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(
        text="Подробнее",
        callback_data=show_domen.new(show="more", name=url)
    )
    markup.insert(button)
    return markup
