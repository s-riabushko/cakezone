from django.contrib import admin
from .models import CommonOption, Counter, Testimonial

# admin.site.register(CommonOption)


@admin.register(CommonOption)
class CommonOption(admin.ModelAdmin):
    list_display = ('key', 'value', 'photo')
    list_filter = ('key',)
    search_fields = ('key', 'value')
    list_editable = ('value', 'photo')


@admin.register(Counter)
class Counter(admin.ModelAdmin):
    list_display = ('name', 'value', 'fa_link', 'is_visible')
    list_filter = ('name', 'fa_link', 'is_visible')
    search_fields = ('name', 'value', 'fa_link')
    list_editable = ('value', 'fa_link', 'is_visible')


@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    list_display = ('photo', 'name', 'profession', 'testimonial_text', 'testimonial_date', 'sort', 'is_visible')
    list_filter = ('name', 'profession', 'is_visible')
    search_fields = ('name', 'profession', 'testimonial_text', 'testimonial_date')
    list_editable = ('name', 'profession', 'testimonial_text', 'testimonial_date', 'sort', 'is_visible')
