import cloudscraper
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    )
}

URLS = [
    "https://www.investing.com/news/cryptocurrency-news",
    "https://www.investing.com/news/economic-indicators",
    "https://www.investing.com/news/economy",
    "https://www.investing.com/news/world-news"
]

scraper = cloudscraper.create_scraper(
    browser={
        "browser": "chrome",
        "platform": "windows",
        "mobile": False
    }
)


def get_article_text(url):

    try:

        response = scraper.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        paragraphs = soup.find_all("p")

        text = []

        for p in paragraphs:

            content = p.get_text(strip=True)

            if len(content) > 40:
                text.append(content)

        return "\n".join(text[:30])

    except Exception as e:

        print("ARTICLE ERROR:", e)

        return ""


def parse_news_page(url):

    result = []

    try:

        response = scraper.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        print("STATUS:", response.status_code)
        print("URL:", response.url)

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        articles = soup.find_all("article")

        print("ARTICLES FOUND:", len(articles))

        for article in articles[:3]:

            a = article.find("a")

            if not a:
                continue

            title = a.get_text(strip=True)

            link = a.get("href")

            if not link:
                continue

            if not link.startswith("http"):
                link = f"https://www.investing.com{link}"

            result.append(
                {
                    "id": link,
                    "title": title,
                    "url": link
                }
            )

    except Exception as e:

        print("PARSER ERROR:", e)

    return result


def get_latest_news():

    news = []

    for url in URLS:

        page_news = parse_news_page(url)

        news.extend(page_news)

    return news