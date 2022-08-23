import logging
import re
import time
from typing import Pattern, Match

from aiogram import types
from aiogram.utils import markdown
from pyppeteer import launch
from pyppeteer.browser import Browser
from pyppeteer.element_handle import ElementHandle
from pyppeteer.page import Page

from keyboards.inline import (
    show_domen,
    check_info
)
from utils.commands import add_item
from utils.config import dp, DOWNLOAD_DIR
from utils.constants import PATTERN
from utils.exceptions import BrowserNotFound
from services.logger import get_log


get_log()


async def search(url: str, msg: int, user_id: int) -> None:
    """
    Процесс формирования скриншота:
    1. запуск браузера в фоне;
    2. получение и отправка скриншота пользователю (группу);
    3. формирование текста (описание скриншота);
    4. редактирование п.2 (добавление п.3);
    5. запись информации в БД.
    """
    start: time = time.perf_counter()
    logging.info("Запуск браузера")
    try:
        browser: Browser = await launch(
           {
               # "executablePath": '/root/.local/share/pyppeteer/local-chromium/588429',
               'headless': True,
               'options': {
                   'args': ['--no-sandbox', '--disable-setuid-sandbox']
               }
           }
        )
    except BrowserNotFound as err:
        logging.error(f"Ошибка запуска браузера\n{err}")
    else:
        page: Page = await browser.newPage()
        await page.goto(
            url,
            {"waitUntil": "networkidle2"}
        )
        file_name: str = url.split('//')[1].rsplit('.')[0]
        path: str = fr"{DOWNLOAD_DIR}\{file_name}.png"
        logging.info("Формирование скриншота в директорию downloads/images")
        await page.screenshot(
            {
                "path": path,
            }
        )
        element: ElementHandle | None = await page.querySelector('title')
        title: str = await page.evaluate(
            '(element) => element.textContent',
            element
        )
        text: str = "\n".join(
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
        logging.info("Пользователь получил ответ (фото)")
        markup = await check_info(5)  # Инлайн-кнопка "Подробнее"
        await dp.bot.edit_message_caption(
            chat_id=user_id,
            message_id=msg,
            caption=text.format(int(time.perf_counter() - start)),
            reply_markup=markup,
            parse_mode='html'
        )
        logging.info("Пользователь получил ответ (фото + текст)")
        pattern: Pattern[str] = re.compile(PATTERN)
        url: Match[str] | None = pattern.search(url)
        await add_item(
            user_id=user_id,
            domen=url.groups("domen")[0]
        )
        logging.info("В БД записана информация")
        await browser.close()


@dp.callback_query_handler(show_domen.filter(show="more"))
async def more_info(call: types.CallbackQuery, callback_data):
    print(callback_data)
    # async with aiohttp.ClientSession() as session:
    #     response = await session.get(url)
    #     print(response.status)

