import feedparser
from datetime import date
from .models import Currency, ExchangeRate
from .currencies_config import CURRENCIES

def get_exchange_rates(currency_code: str):
    feed = feedparser.parse(f'https://www.ecb.europa.eu/rss/fxref-{currency_code.lower()}.html')
    return [
        (date.fromisoformat(entry['updated'][:10]), entry['cb_exchangerate'].split()[0])
        for entry in feed.entries
    ]


def update_exchange_rates(currency_code: str):
    currency = Currency.objects.get(code=currency_code)
    for date, rate in get_exchange_rates(currency_code):
        exchange_rate = ExchangeRate.objects.filter(currency=currency, date=date).first()
        if not exchange_rate:
            new_exchange_rate = ExchangeRate(date=date, rate=rate, currency=currency)
            new_exchange_rate.save()


def update_all_currencies():
    for currency_code in CURRENCIES:
        update_exchange_rates(currency_code)
