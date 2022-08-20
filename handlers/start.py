import time
from aiogram import types
from aiogram.utils import markdown

from config import dp, DOWNLOAD_DIR
from pyppeteer import launch

from utils.commands import add_item
from utils.exceptions import check_connect


@dp.message_handler(commands=("start",))
async def start(message):
    await message.answer(text="hi")


@dp.message_handler()
async def search(message):
    try:
        url = message.text
        if not url.startswith(("https", "http")):
            raise Exception
    except Exception:
        print("q")
    else:
        msg = await message.reply_photo(
            photo="https://sun9-85.userapi.com/impg/qfz8AxGHPJt-oMfwAnvM17LlvaRK9jIhC3FAvQ/vexkCYmaXY4.jpg?size=676x694&quality=96&sign=0128240c61865b40f3f4bcafcec9a5c9&type=album",
            caption="Запрос принят",
            reply=False
        )
        target = await check_connect(url)
        if not target:
            return
        start = time.perf_counter()
        browser = await launch()
        page = await browser.newPage()
        await page.goto(
            url,
            {"waitUntil": "networkidle2"}
        )
        path = f"{DOWNLOAD_DIR}\google.png"
        await page.screenshot(
            {
                "path": path,
            }
        )
        element = await page.querySelector('title')
        title = await page.evaluate('(element) => element.textContent', element)
        text = "\n".join(
            (
                title,
                f"\n{markdown.hbold('Веб - сайт')}: {url}\n",
                "Время обработки: {} секунд"
            )
        )
        with open(path, 'rb') as file:
            await dp.bot.edit_message_media(
                chat_id=message.from_user.id,
                message_id=msg.message_id,
                media=types.InputMediaPhoto(file)
            )
        await dp.bot.edit_message_caption(
            chat_id=message.from_user.id,
            message_id=msg.message_id,
            caption=text.format(int(time.perf_counter() - start)),
            parse_mode='html'
        )
        await add_item(
            user_id=1,
            domen="q"
        )
        await browser.close()
