from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def check_news_relevance(title, article_text):

    prompt = f"""
Ты редактор крупного криптовалютного Telegram канала.

Оцени новость.

Заголовок:
{title}

Текст:
{article_text}

Если новость может повлиять на:

- Bitcoin
- Ethereum
- Крипторынок
- ETF
- ФРС
- Процентные ставки
- Инфляцию
- Доллар США
- Банковскую систему
- Ликвидность
- Регулирование криптовалют

Ответь строго:

YES|ВАЖНОСТЬ

Пример:

YES|9

Если новость не важна:

NO|0

Без объяснений.
"""

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content.strip()

    try:

        status, score = result.split("|")

        return {
            "approved": status == "YES",
            "score": int(score)
        }

    except:

        return {
            "approved": False,
            "score": 0
        }