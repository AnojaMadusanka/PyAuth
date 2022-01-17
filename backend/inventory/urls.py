from django.urls import path

from .views import getSales

urlpatterns = [
    path('sales', getSales, name='sales'),
]