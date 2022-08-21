import os

from pathlib import Path
from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv


load_dotenv()

bot: Bot = Bot(os.getenv("BOT_TOKEN"))
dp: Dispatcher = Dispatcher(bot)

BASE_DIR = Path(__file__).parent.parent
DOWNLOAD_DIR = BASE_DIR / "downloads" / "images"
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
