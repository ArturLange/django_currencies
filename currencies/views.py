from django.http import JsonResponse
import feedparser
from decimal import Decimal

def index(request):
    return JsonResponse({})

def currency(request, currency_code: str):
    feed = feedparser.parse(f'https://www.ecb.europa.eu/rss/fxref-{currency_code.lower()}.html')
    amount = Decimal(feed.entries[0]['cb_exchangerate'].split()[0])
    return JsonResponse({
        'currency_code': currency_code.upper(),
        'exchange_rate': amount
    }, json_dumps_params={'default': float})
