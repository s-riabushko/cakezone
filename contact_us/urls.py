from django.urls import path
from .views import index

app_name = 'contact_us'

urlpatterns = [
    path('', index, name='index'),
]
