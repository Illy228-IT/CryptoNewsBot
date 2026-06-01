from telegram import Bot
from config import BOT_TOKEN, CHANNEL_ID

bot = Bot(token=BOT_TOKEN)


async def publish_post(text):
    try:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=text,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

        print("Telegram message sent")

    except Exception as e:
        print(f"Telegram error: {e}")