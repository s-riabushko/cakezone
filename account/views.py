from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/successful_register'


class MyLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return self.request.GET.get('next', '/')


def user_logout(request):
    logout(request)
    return redirect('home:index')


def successful_register(request):
    return render(request, 'successful_register.html')
