import requests

from config import NEWS_API_KEY


QUERIES = [
    "Bitcoin OR Ethereum OR Crypto OR Cryptocurrency",
    "Crypto market OR Bitcoin analysis OR Ethereum analysis",
    "Economy OR Inflation OR Interest Rates OR Central Bank",
    "GDP OR CPI OR PPI OR Unemployment OR Inflation Data",
    "Geopolitics OR World News OR International Relations"
]


def get_article_text(url):
    return url


def get_latest_news():

    news = []

    headers = {
        "X-Api-Key": NEWS_API_KEY
    }

    for query in QUERIES:

        try:

            response = requests.get(
                "https://newsapi.org/v2/everything",
                params={
                    "q": query,
                    "language": "en",
                    "sortBy": "publishedAt",
                    "pageSize": 5
                },
                headers=headers,
                timeout=20
            )

            data = response.json()

            if data.get("status") != "ok":
                print(data)
                continue

            for article in data["articles"]:

                title = article.get("title")

                url = article.get("url")

                description = article.get("description", "")

                if not title or not url:
                    continue

                news.append(
                    {
                        "id": url,
                        "title": title,
                        "url": url,
                        "description": description
                    }
                )

        except Exception as e:

            print("NEWS API ERROR:", e)

    unique_news = []

    seen = set()

    for item in news:

        if item["id"] in seen:
            continue

        seen.add(item["id"])

        unique_news.append(item)

    print(f"Found news: {len(unique_news)}")

    return unique_news


def get_article_text(url):
    return url
