from aiogram.utils.markdown import hbold

HELLO_TEXT = (
    (
        f"Привет! Меня зовут {hbold('tp - lab')}.",
        "Я - Бот для создания веб-скриншотов.",
        "Чтобы получить скриншот - отправьте URL адрес сайта. Например, "
        "wikipedia.org\n",
        f"Бот использузет {hbold('chromedriver')}.",
        f"Работает с протоколами {hbold('http')}, {hbold('https')}"
    )
)

PATTERN = r"//(?P<domen>[\w\d]+.*)/?"

DOMEN_URL = "https://whois.ru/{domen}"

DT_FORMAT = '%d.%m.%Y %H:%M:%S'

LOG_FORMAT = "".join(
    (
        "|\t%(asctime)s – [%(levelname)s]: %(message)s. ",
        "Исполняемый файл – '%(filename)s': ",
        "функция – '%(funcName)s'(%(lineno)d)"
    )
)

ERROR_REQUEST = "\n".join(
    (
        "В запросе допущена ошибка. Проверьте правильность ссылки",
        "Шаблон: http(s)://<домен>"
    )
)
