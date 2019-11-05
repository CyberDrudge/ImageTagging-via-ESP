from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import LoginForm, RegisterForm


User = get_user_model()


# Create your views here.
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("Error")
    return render(request, "accounts/login.html", context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(
            username=username,
            password=password,
        )
        return redirect('/')
    return render(request, "accounts/register.html", context)
