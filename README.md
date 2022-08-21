# Теlegram-bot

## Описание

Бот для создания скриншотов веб-сайтов по заданной ссылке. Например, скинув `https://github.com` боту, будет сделан
скриншот заданного `url`.  
Бот работает как в личным, так и групповых чатах.

## Содержание

- [Технологии](#технологии)
- <a href="#t1">Структура проекта</a>
- Запуск
- [Автор](#автор)

## Технологии
- Python
- Aiogram
- Django
- PostgreSQL
- Pyppeteer

<details>
  <summary>
      <h2 id="t1">Структура проекта</h2>
  </summary>

```cmd
 tp-lab:
|   .env
|   .gitignore
|   django_app.py  <-- копия файла manage.py (для запуска из главной директории)
|   LICENSE
|   main.py  <-- Точка входа (запуск бота)
|   README.md
|   requirements.txt
|   tree.txt
|
+---adminpanel  <-- Django проект
|   |   manage.py
|   |   
|   +---adminpanel
|   |   |   asgi.py
|   |   |   settings.py
|   |   |   urls.py
|   |   |   wsgi.py
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           
|   +---panel  <-- Django приложение
|   |   |   admin.py  <-- админ-панель superuser
|   |   |   apps.py
|   |   |   models.py  <-- модель БД
|   |   |   tests.py
|   |   |   views.py
|   |   |   __init__.py
|   |   |           
|   |   \---__pycache__
|   |           
|   \---__pycache__
|           
+---downloads  <-- Директория с сохранёнными скриншотами
|   \---images
|           
+---handlers  <-- Обработчики updates
|   |   parse_and_answer.py  <-- Обработка запроса
|   |   start.py  <-- Проверка запроса + описание бота (/start)
|   |   __init__.py
|   |   
|   \---__pycache__
|           
+---keyboards  <-- Клавиатуры
|   |   inline.py  <-- Инлайн кнопки
|   |   __init__.py
|   |   
|   \---__pycache__
|           
+---services
|   |   logger.py  <-- Логгер
|   |   __init__.py
|   |   
|   \---__pycache__
|           
+---utils
|   |   commands.py  <-- Команды для работы с БД через бота
|   |   config.py  <-- Конфигурация бота и директорий
|   |   constants.py  <-- Константные данные
|   |   exceptions.py  <-- Кастомные исключения
|   |   misc.py  <-- Обработка ошибок
|   |   __init__.py
|   |   
|   \---__pycache__
|           
+---venv
|
\---__pycache__
```

</details>

## Запуск

## Автор

[Mikhail Kushnerev](https://github.com/Mikhail-Kushnerev/)  
[⬆️В начало](#telegram-bot)