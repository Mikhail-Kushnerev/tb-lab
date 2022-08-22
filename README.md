# Теlegram-bot

## Описание

Бот для создания скриншотов веб-сайтов по заданной ссылке. Например, скинув `https://github.com` боту, будет сделан
скриншот заданного `url`.  
Бот работает как в личным, так и групповых чатах.

## Содержание

- [Технологии](#технологии)
- <a href="#t1">Структура проекта</a>
- [Запуск](#запуск)
- [Автор](#автор)

## Технологии
- Python
- Aiogram
- Pyppeteer
- Django
- PostgreSQL
- Docker


<details>
  <summary>
      <h2 id="t1">Структура проекта</h2>
  </summary>

```cmd
tp-lab:
|   .gitignore
|   LICENSE
|   README.md
|           
+---src
|   |   django_app.py  <-- копия файла manage.py (для запуска из главной директории)
|   |   docker-compose.yml
|   |   Dockerfile
|   |   main.py  <-- Точка входа (запуск бота)
|   |   requirements.txt
|   |   __init__.py
|   |   
|   +---adminpanel  <-- Django проект
|   |   |   manage.py
|   |   |   __init__.py
|   |   |   
|   |   +---adminpanel
|   |   |   |   asgi.py
|   |   |   |   settings.py
|   |   |   |   urls.py
|   |   |   |   wsgi.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           
|   |   +---panel  <-- Django приложение
|   |   |   |   admin.py  <-- админ-панель superuser
|   |   |   |   apps.py
|   |   |   |   models.py  <-- модель БД
|   |   |   |   tests.py
|   |   |   |   views.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---migrations
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           
|   |   \---__pycache__
|   |           
|   +---downloads  <-- Директория с сохранёнными скриншотами
|   |   \---images
|   |           
|   +---handlers  <-- Обработчики updates
|   |   |   parse_and_answer.py  <-- Обработка запроса
|   |   |   start.py  <-- Проверка запроса + описание бота (/start)
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           
|   +---keyboards  <-- Клавиатуры
|   |   |   inline.py  <-- Инлайн кнопки
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           
|   +---services
|   |   |   logger.py  <-- Логгер
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           
|   +---utils
|   |   |   commands.py  <-- Команды для работы с БД через бота
|   |   |   config.py  <-- Конфигурация бота и директорий
|   |   |   constants.py  <-- Константные данные
|   |   |   exceptions.py  <-- Кастомные исключения
|   |   |   misc.py  <-- Обработка ошибок
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           
|   \---__pycache__
```

</details>

## Запуск

Для запуска необходим токен телеграмм-бота. В случае его отсутствия создайте бота с помощью @BotFather
- Создайте и запустите вирт. окружения:
```python
python -m venv venv
(win) source venv/Scripts/activate
(linux) source venv/bin/activate
```
- Установите зависимости из главной директории:
```python
pip install -r requirements.txt
```
- Создайте токен для `Django`-проекта:
```python
(главная директория)
python django_app.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
Output:
    'ed6%d)b9i%k0ohg6^ql8q+8vrawvb__&45vr*&s&nrqu7ma&y&'
```
- Создайте и заполните `.env` файл в директории `src`. Пример:
```dotenv
BOT_TOKEN="<токен телеграмм-бота от @BotFather>"

SECRET_KEY="ed6%d)b9i%k0ohg6^ql8q+8vrawvb__&45vr*&s&nrqu7ma&y&"

DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
- Из директории `src` выполните команду:
```python
docker-compose up
```

## Автор

[Mikhail Kushnerev](https://github.com/Mikhail-Kushnerev/)  
[⬆️В начало](#telegram-bot)