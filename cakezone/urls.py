"""
URL configuration for cakezone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from main.views import main_index
from menu.views import menu_index
from team.views import team_index
from service.views import service_index
from contact.views import contact_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', menu_index, name='menu_index'),
    path('team/', team_index, name='team_index'),
    path('service/', service_index, name='service_index'),
    path('contact/', contact_index, name='contact_index'),
    path('', main_index, name='main_index'),
]
