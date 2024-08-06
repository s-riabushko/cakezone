from django.shortcuts import render


# Create your views here.
def team_index(request):
    return render(request, "team.html")
