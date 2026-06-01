import json
import os

DB_FILE = "data/posted_news.json"


def load_news():

    if not os.path.exists(DB_FILE):
        return []

    try:

        with open(
            DB_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []


def save_news(news_list):

    with open(
        DB_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            news_list,
            file,
            ensure_ascii=False,
            indent=4
        )


def is_posted(news_id):

    news = load_news()

    return news_id in news


def mark_posted(news_id):

    news = load_news()

    if news_id not in news:

        news.append(news_id)

        save_news(news)


def initialize_news(news_list):

    if os.path.exists(DB_FILE):
        return

    ids = []

    for news in news_list:

        ids.append(news["id"])

    save_news(ids)

    print(
        f"Initialized database with "
        f"{len(ids)} news"
    )