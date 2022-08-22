from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


show_domen: CallbackData = CallbackData("info", "show", "name")


async def check_info(url: str) -> InlineKeyboardMarkup:
    markup: InlineKeyboardMarkup = InlineKeyboardMarkup()

    button: InlineKeyboardButton = InlineKeyboardButton(
        text="Подробнее",
        callback_data=show_domen.new(show="more", name=url)
    )
    markup.insert(button)
    return markup
