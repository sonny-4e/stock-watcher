from dotenv import load_dotenv
import os

load_dotenv()

WATCHLIST = ["AAPL", "MSFT", "NVDA"]


def get_api_key() -> str:
    klucz = os.getenv("FINNHUB_API_KEY")
    if not klucz:
        raise RuntimeError("Brak FINNHUB_API_KEY — dodaj go do pliku .env")
    return klucz
