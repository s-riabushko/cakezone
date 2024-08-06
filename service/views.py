from django.shortcuts import render


# Create your views here.
def service_index(request):
    return render(request, "service.html")
