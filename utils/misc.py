import logging

import aiohttp
from aiohttp import ClientResponse
from requests.exceptions import RequestException

from services.logger import get_log

get_log()


async def check_connect(url):
    try:
        async with aiohttp.ClientSession() as session:
            response: ClientResponse = await session.get(url)
            if (status := response.status) == 400:
                raise RequestException
    except RequestException:
        logging.error("Ошибка в запросе. Запрос отменён")
    else:
        logging.info(f"Корректная ссылка. Статус {status}")
        return True
