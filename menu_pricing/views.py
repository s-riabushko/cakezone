from django.shortcuts import render
from django.http import HttpResponse

from menu_pricing.models import Category


# Create your views here.
def index(request):
    categories = Category.objects.filter(is_visible=True)
    context = {
        'categories': categories
    }
    return render(request, 'menu_pricing.html', context=context)
