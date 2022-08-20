import re
import time

from aiogram import types
from aiogram.utils import markdown
from pyppeteer import launch

from config import dp, DOWNLOAD_DIR
from constants import PATTERN
from utils.commands import add_item


async def search(url, msg, user_id):
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
            chat_id=user_id,
            message_id=msg,
            media=types.InputMediaPhoto(file)
        )
    await dp.bot.edit_message_caption(
        chat_id=user_id,
        message_id=msg,
        caption=text.format(int(time.perf_counter() - start)),
        parse_mode='html'
    )
    compile = re.compile(PATTERN)
    domen = compile.search(url)
    await add_item(
        user_id=user_id,
        domen=domen.groups("domen")[0]
    )
    await browser.close()