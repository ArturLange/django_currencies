from django.urls import path

from . import views

app_name = 'currencies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:currency_code>', views.currency, name='currency')
]
