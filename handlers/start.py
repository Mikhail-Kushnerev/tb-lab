import re

from config import dp, BASE_DIR, DOWNLOAD_DIR
from pyppeteer import launch

from constants import PATTERN
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
        msg = await message.answer("Запрос принят")
        target = await check_connect(url)
        if not target:
            return
        browser = await launch()
        page = await browser.newPage()
        await page.goto(
            url,
            {"waitUntil": "networkidle2"}
        )
        await page.screenshot(
            {
                "path": f"{DOWNLOAD_DIR}\google.png",
            }
        )
        element = await page.querySelector('title')
        title = await page.evaluate('(element) => element.textContent', element)
        text = "\n".join(
            (
                title,
                url,
                "time"
            )
        )
        await dp.bot.edit_message_text(
            chat_id=message.from_user.id,
            message_id=msg.message_id,
            text=text
        )
        await browser.close()
