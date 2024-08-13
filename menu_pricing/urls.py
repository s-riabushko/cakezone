from django.urls import path
from .views import index

app_name = 'menu_pricing'

urlpatterns = [
    path('', index, name='index'),
]
