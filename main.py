import os

from aiogram import executor


def setup_django():
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

    try:
        setup_django()
    except Exception:
        ...
    from handlers import dp
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception:
        ...
