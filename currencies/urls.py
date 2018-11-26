from django.urls import path

from . import views

app_name = 'currencies'
urlpatterns = [
    path('', views.all_currencies, name='all_currencies'),
    path('<str:currency_code>', views.currency, name='currency')
]
