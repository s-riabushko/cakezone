from django.contrib import admin
from .models import Category, Dish
from django.utils.safestring import mark_safe

# Register your models here.
# admin.site.register(Category)


class DishInline(admin.TabularInline):
    model = Dish
    fields = ('name', 'price', 'is_visible', 'sort')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (DishInline, )
    list_display = ('name', 'description', 'sort', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('name', 'description')
    list_editable = ('description', 'sort', 'is_visible')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_tag', 'category', 'name', 'price', 'is_special', 'is_visible')
    list_filter = ('is_visible', 'is_special', 'category')
    search_fields = ('name', 'price')
    list_editable = ('name', 'price', 'is_special', 'is_visible')

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"  height="50"/>')

    photo_tag.short_description = 'Photo'
