import requests
from stock_watcher.config import get_api_key

BASE_URL = "https://finnhub.io/api/v1"
TIMEOUT = 10


def get_quote(ticker: str) -> dict:
    url = BASE_URL + "/quote"
    params = {"symbol": ticker}
    headers = {"X-Finnhub-Token": get_api_key()}

    odpowiedz = requests.get(url=url, params=params, headers=headers, timeout=TIMEOUT)
    odpowiedz.raise_for_status()

    dane = odpowiedz.json()

    if dane["c"] == 0:
        raise ValueError(f"Nieznany ticker: {ticker}")

    return {
        "ticker": ticker,
        "price": dane["c"],
        "change": dane["d"],
        "change_pct": dane["dp"],
        "high": dane["h"],
        "low": dane["l"],
        "open": dane["o"],
        "prev_close": dane["pc"],
    }


if __name__ == "__main__":
    from stock_watcher.config import WATCHLIST

    for ticker in WATCHLIST:
        quote = get_quote(ticker)
        print(
            f"{quote['ticker']:<6} {quote['price']:>10.2f} {quote['change_pct']:+.2f}%"
        )
