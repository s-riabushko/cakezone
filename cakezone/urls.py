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
from django.urls import path, re_path, include
from django.conf.urls.static import static
from cakezone import settings
from contacts.views import subscribe as contacts_subscribe
from account.views import RegisterView, MyLoginView, user_logout, successful_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('menu/', include('menu.urls')),
    path('masters/', include('masters.urls')),
    path('services/', include('services.urls')),
    path('contacts/', include('contacts.urls')),
    path('subscribe/', contacts_subscribe, name='contacts_subscribe'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('successful_register/', successful_register, name='successful_register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
