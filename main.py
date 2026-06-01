import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.storage import initialize_news
from parser.investing_parser import (
    get_latest_news,
    get_article_text
)

from ai.post_generator import generate_post
from ai.news_filter import check_news_relevance

from tg.publisher import publish_post

from utils.storage import (
    is_posted,
    mark_posted
)

MAX_POSTS_PER_RUN = 3


async def process_news():

    print("\n========== CHECKING NEWS ==========\n")

    news_list = get_latest_news()
    initialize_news(news_list)

    print(f"Found news: {len(news_list)}")

    posted_count = 0

    for news in news_list:

        if posted_count >= MAX_POSTS_PER_RUN:
            print("Post limit reached")
            break

        try:

            if is_posted(news["id"]):
                continue

            print(f"\nProcessing: {news['title']}")

            article_text = get_article_text(
                news["url"]
            )

            if not article_text:
                print("Article text not found")
                continue

            check = check_news_relevance(
                news["title"],
                article_text
            )

            print(
                f"Filter result: "
                f"approved={check['approved']} "
                f"score={check['score']}"
            )

            if not check["approved"]:
                print("Skipped by AI filter")
                continue

            if check["score"] < 8:
                print("Skipped because score < 8")
                continue

            post = generate_post(
                news["title"],
                article_text
            )

            await publish_post(post)

            mark_posted(news["id"])

            posted_count += 1

            print(
                f"SUCCESSFULLY POSTED ({posted_count}/{MAX_POSTS_PER_RUN})"
            )

            await asyncio.sleep(120)

        except Exception as e:

            print(
                f"ERROR WHILE PROCESSING "
                f"{news['title']}"
            )

            print(e)


async def main():

    print("BOT STARTED")

    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        process_news,
        "interval",
        minutes=30,
        max_instances=1
    )

    scheduler.start()

    await process_news()

    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())