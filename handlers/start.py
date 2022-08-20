from config import dp
from constants import HELLO_TEXT
from utils.exceptions import check_connect
from handlers.parse_and_answer import search

@dp.message_handler(commands=("start",))
async def start(message):
    await message.answer(
        "\n".join(HELLO_TEXT),
        parse_mode="html"
    )


@dp.message_handler()
async def check(message):
    try:
        url = message.text
        if not url.startswith(("https", "http")):
            raise Exception
        target = await check_connect(url)
        if not target:
            raise Exception
    except Exception:
        print("q")
    else:
        msg = await message.reply_photo(
            photo="https://sun9-85.userapi.com/impg/qfz8AxGHPJt-oMfwAnvM17LlvaRK9jIhC3FAvQ/vexkCYmaXY4.jpg?size=676x694&quality=96&sign=0128240c61865b40f3f4bcafcec9a5c9&type=album",
            caption="Запрос принят",
            reply=False
        )
        await search(url, msg.message_id, message.from_user.id)
