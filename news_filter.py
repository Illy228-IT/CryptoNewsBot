# news_filter.py

IMPORTANT_WORDS = [
    "bitcoin",
    "btc",
    "ethereum",
    "eth",
    "etf",
    "sec",
    "cftc",
    "fed",
    "fomc",
    "interest rate",
    "cpi",
    "inflation",
    "binance",
    "coinbase",
    "bybit",
    "hack",
    "exploit",
    "lawsuit",
    "liquidation",
    "bankruptcy",
    "blackrock",
    "microstrategy",
    "institutional",
    "whale",
]

BAD_WORDS = [
    "nft",
    "airdrop",
    "giveaway",
    "meme",
    "memecoin",
    "price prediction",
    "analyst says",
    "partnership",
    "gaming token",
]


def cheap_crypto_filter(title, text=""):
    content = f"{title} {text}".lower()

    if any(word in content for word in BAD_WORDS):
        return False

    return any(word in content for word in IMPORTANT_WORDS)