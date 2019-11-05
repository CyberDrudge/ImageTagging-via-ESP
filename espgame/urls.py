"""espgame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from game.views import homepage, thegame, action
from accounts.views import login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('play', thegame, name='thegame'),
    path('action', action, name='action'),
    path('login', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register', register_page, name='register'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
