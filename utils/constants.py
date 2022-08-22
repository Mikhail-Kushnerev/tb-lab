from aiogram.utils.markdown import hbold

HELLO_TEXT: tuple[str, ...] = (
    (
        f"Привет! Меня зовут {hbold('tp - lab')}.",
        "Я - Бот для создания веб-скриншотов.",
        "Чтобы получить скриншот - отправьте URL адрес сайта. Например, "
        "wikipedia.org\n",
        "Вы также можете добавить меня в свои чаты, и я смогу "
        "проверять ссылки других пользователей\n",
        f"Бот использузет {hbold('chromedriver')}.",
        f"Работает с протоколами {hbold('http')}, {hbold('https')}"
    )
)

DEFAULT_ANSWER_PIC = "https://clck.ru/toTTE"

PATTERN: str = r"//(?P<domen>[\w\d]+.*)/?"

DOMEN_URL: str = "https://whois.ru/{domen}"

DT_FORMAT: str = '%d.%m.%Y %H:%M:%S'

LOG_FORMAT: str = "".join(
    (
        "|\t%(asctime)s – [%(levelname)s]: %(message)s. ",
        "Исполняемый файл – '%(filename)s': ",
        "функция – '%(funcName)s'(%(lineno)d)"
    )
)

ERROR_REQUEST: str = "\n".join(
    (
        "В запросе допущена ошибка. Проверьте правильность ссылки",
        "Шаблон: http(s)://<домен>"
    )
)
