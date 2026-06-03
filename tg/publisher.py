from telegram import Bot

from config import (
    BOT_TOKEN,
    CHANNEL_IDS
)

bot = Bot(token=BOT_TOKEN)


async def publish_post(text):

    try:

        for channel in CHANNEL_IDS:

            if not channel:
                continue

            await bot.send_message(
                chat_id=channel,
                text=text,
                parse_mode="HTML",
                disable_web_page_preview=True
            )

            print(
                f"Telegram message sent to "
                f"{channel}"
            )

    except Exception as e:

        print(
            f"Telegram error: {e}"
        )
