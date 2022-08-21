import logging
import os

from aiogram import executor

from services.logger import get_log


def setup_django() -> None:
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "adminpanel.adminpanel.settings"
    )
    os.environ.update(
        {
            "DJANGO_ALLOW_ASYNC_UNSAFE": "true"
        }
    )
    import django
    django.setup()


if __name__ == "__main__":
    get_log()
    try:
        setup_django()
    except Exception:
        logging.error("Сбой подключения Django к боту")
    else:
        logging.info("Django подключен к боту")

    from handlers import dp
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception:
        logging.error("Ошибка запуска бота")
    else:
        logging.info("Бот запущен")
