# Currencies API

## Description

There are 3 views:

- `/api/currencies/` - get all currencies with latest exchange rates
- `/api/currencies/<currency>/latest` - get latest exchange rate for one currency (provide currency code e.g. USD)
- `/api/currencies/<currency>` - get exchange rates for one currency - returns all exchange rates unless filtered. Can be filtered by `start_date` or `end_date` e.g. `/api/currencies/USD?start_date=2018-11-22&end_date=2018-11-25`

These views return exchange rates with EUR as base. At the moment database is updated only when request is done (before responding).

### TODOs

- Add pagination
- Implement periodic checking for updates instead of updating on request (Celery Beat maybe?)
- Add error handling for invalid requests (no handling at all at the moment - `/api/currencies/BTC` will return 500 and adding new currency through Django admin will break `/api/currencies/` view 😆)
- Add tests (no tests at all at the moment)
- Configure PostgreSQL instead of sqlite
- ...

## Setup

### Prerequisites

- Python >= 3.6
- virtualenv (optional)

### Steps

1. `pip install -r requirements.txt`
2. `python3 manage.py migrate`
3. `python3 manage.py loaddata currencies_dump.json`
4. `python3 manage.py runserver`
