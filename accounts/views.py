from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import DetailView, UpdateView
from .forms import LoginForm, RegisterForm, UpdateProfileForm
from .models import Player

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


class AccountHomeView(DetailView):
    template_name = 'accounts/home.html'

    def get_object(self):
        user = self.request.user
        qs, new = Player.objects.new_or_get(user=user)
        return qs


class ProfileView(UpdateView):
    template_name = 'accounts/profile.html'
    form_class = UpdateProfileForm

    def get_object(self):
        user = self.request.user
        qs, new = Player.objects.new_or_get(user=user)
        return qs

    def get_success_url(self):
        return reverse("account:home")
