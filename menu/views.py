from django.shortcuts import render


# Create your views here.
def menu_index(request):
    return render(request, "menu.html")
