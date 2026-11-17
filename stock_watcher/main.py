import logging
from stock_watcher.config import WATCHLIST
from stock_watcher.finnhub_client import get_quote

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

logger = logging.getLogger(__name__)


def fetch_all(tickers: list[str]) -> list[dict]:
    wyniki = []
    for ticker in tickers:
        try:
            quote = get_quote(ticker)
            wyniki.append(quote)
            logger.info(f"{ticker}: {quote['price']:.2f} ({quote['change_pct']:+.2f}%)")

        except Exception as e:
            logger.error(f"{ticker}: nie udało się pobrać — {e}")
    return wyniki


def run() -> list[dict]:
    logger.info(f"Start - sprawdzam {len(WATCHLIST)} tickerów")
    quotes = fetch_all(WATCHLIST)
    logger.info(f"Pobrano {len(quotes)} z {len(WATCHLIST)}")
    return quotes


if __name__ == "__main__":
    run()
