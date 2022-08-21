import logging

import aiohttp
from requests.exceptions import RequestException

from services.logger import get_log

get_log()


async def check_connect(url):
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            if (status := response.status) == 400:
                raise RequestException
    except RequestException:
        logging.error("Ошибка в запросе. Запрос отменён")
    else:
        logging.info(f"Корректная ссылка. Статус {status}")
        return True
