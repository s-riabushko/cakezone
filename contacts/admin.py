from django.contrib import admin
from .models import Contacts


# Register your models here.
@admin.register(Contacts)
class Contacts(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'facebook', 'twitter', 'linkedin', 'is_visible')
    list_editable = ('phone', 'email', 'is_visible')
