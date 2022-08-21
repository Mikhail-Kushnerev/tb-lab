import re
import time

import aiohttp
from aiogram import types
from aiogram.utils import markdown
from pyppeteer import launch

from config import dp, DOWNLOAD_DIR
from constants import PATTERN
from utils.commands import add_item
from keyboards.inline import (
    show_domen,
    check_info
)


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
    markup = await check_info(5)
    await dp.bot.edit_message_caption(
        chat_id=user_id,
        message_id=msg,
        caption=text.format(int(time.perf_counter() - start)),
        reply_markup=markup,
        parse_mode='html'
    )
    compile = re.compile(PATTERN)
    domen = compile.search(url)
    await add_item(
        user_id=user_id,
        domen=domen.groups("domen")[0]
    )
    await browser.close()


@dp.callback_query_handler(show_domen.filter(show="more"))
async def more_info(call: types.CallbackQuery, callback_data):
    print(callback_data)
    # async with aiohttp.ClientSession() as session:
    #     response = await session.get(url)
    #     print(response.status)

