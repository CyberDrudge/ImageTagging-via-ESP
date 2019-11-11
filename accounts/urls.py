from django.urls import path
from .views import AccountHomeView, ProfileView

app_name = "accounts"

urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
