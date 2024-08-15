from django.shortcuts import render
from .models import Staff


# Create your views here.
def index(request):
    staff = Staff.objects.filter(is_visible=True)
    context = {
        'staff': staff
    }
    return render(request, 'staff.html', context=context)
