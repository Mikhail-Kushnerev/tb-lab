import logging

from aiogram.types import Message

from handlers.parse_and_answer import search
from services.logger import get_log
from utils.config import dp
from utils.constants import HELLO_TEXT, ERROR_REQUEST
from utils.exceptions import BrokenUrlStart, BrokenUrl
from utils.misc import check_connect

get_log()


@dp.message_handler(commands=("start",))
async def start(message: Message) -> None:
    user: str = message.from_user.first_name
    logging.info(
        f"Пользователь {user} вызвал команду 'start'"
    )
    await message.answer(
        "\n".join(HELLO_TEXT),
        parse_mode="html"
    )
    logging.info(
        f"Пользователь {user} получил описание работы бота"
    )


@dp.message_handler()
async def check(message: Message) -> None:
    logging.info(f"Запрос от {message.from_user.first_name}")
    try:
        url: str = message.text
        if not url.startswith(("https", "http")):
            raise BrokenUrlStart
        target: bool | None = await check_connect(url)
        if not target:
            raise BrokenUrl
    except BrokenUrlStart:
        logging.error("В запросе отсутствует протокол")
        await message.answer(
            "Убедитесь, что Ваш запрос содержит один из (http, https) протоколов"
        )
    except BrokenUrl:
        logging.error("Не корректная ссылка")
        await message.answer(
            ERROR_REQUEST
        )
    else:
        logging.info("Запрос прошёл проверку")
        msg: Message = await message.reply_photo(
            photo="https://sun9-85.userapi.com/impg/qfz8AxGHPJt-oMfwAnvM17LlvaRK9jIhC3FAvQ/vexkCYmaXY4.jpg?size=676x694&quality=96&sign=0128240c61865b40f3f4bcafcec9a5c9&type=album",
            caption="Запрос принят",
            reply=False
        )
        await search(
            url,
            msg.message_id,
            message.chat.id or message.from_user.id
        )
