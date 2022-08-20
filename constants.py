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
