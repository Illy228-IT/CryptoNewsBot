import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_IDS = [
    os.getenv("CHANNEL_ID_1"),
    os.getenv("CHANNEL_ID_2")
]
