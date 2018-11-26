from django.urls import path

from . import views

app_name = 'currencies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:currency_acronym>', views.currency, name='currency')
]
