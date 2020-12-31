from django.urls import path
from . import views

app_name = 'orders_app'

urlpatterns = [
    path('create/', views.orders_app_create, name='orders_app_create'),
]
