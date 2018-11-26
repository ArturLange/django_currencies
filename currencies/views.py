from django.http import JsonResponse
import feedparser
from decimal import Decimal
from .models import ExchangeRate
from datetime import date
from .scraping import update_exchange_rates

def index(request):
    return JsonResponse({})

def currency(request, currency_code: str):
    update_exchange_rates(currency_code)
    exchange_rate = ExchangeRate.objects.filter(currency__code=currency_code).order_by('-date').first()
    return JsonResponse({
        'currency_code': currency_code.upper(),
        'date': exchange_rate.date.isoformat(),
        'exchange_rate': exchange_rate.rate
    }, json_dumps_params={'default': float})
