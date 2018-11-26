from django.http import JsonResponse
import feedparser
from decimal import Decimal
from .models import ExchangeRate, Currency
from datetime import date
from .scraping import update_exchange_rates


def currency(request, currency_code: str):
    update_exchange_rates(currency_code)

    exchange_rate = ExchangeRate.objects.filter(currency__code=currency_code).order_by('-date').first()
    return JsonResponse({
        'currency_code': currency_code.upper(),
        'date': exchange_rate.date.isoformat(),
        'exchange_rate': exchange_rate.rate
    }, json_dumps_params={'default': float})


def all_currencies(request):
    result = []

    for currency in Currency.objects.all():
        update_exchange_rates(currency.code)
        exchange_rate = currency.exchange_rates.order_by('-date').first()
        result.append(
            {
                'currency_code': currency.code.upper(),
                'date': exchange_rate.date.isoformat(),
                'exchange_rate': exchange_rate.rate
            }
        )

    return JsonResponse(result, safe=False, json_dumps_params={'default': float})
