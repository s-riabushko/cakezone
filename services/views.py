from django.shortcuts import render
from menu.models import Category


# Create your views here.
def index(request):
    services = Category.objects.filter(is_visible=True)
    context = {
        'services': services
    }
    return render(request, 'services.html', context=context)
