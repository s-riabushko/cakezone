from django.contrib import admin
from .models import Contacts, MessageFromCustomer, Subscriber


@admin.register(Contacts)
class Contacts(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'facebook', 'twitter', 'linkedin', 'is_visible')
    list_editable = ('phone', 'email', 'is_visible')


@admin.register(MessageFromCustomer)
class MessageFromCustomer(admin.ModelAdmin):
    list_display = ('email', 'name', 'subject', 'created_at', 'updated_at', 'is_processed')


@admin.register(Subscriber)
class Subscriber(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at', 'updated_at')
