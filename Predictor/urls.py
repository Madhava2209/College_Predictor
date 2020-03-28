"""Predictor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from College_Predictor.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('signup/',signup),
    path('login/',user_login),
    path('logout/',user_logout),
    path('create/',add_college),
    path('all_college/',all_college),
    path('success/',success),
    path('get_list/',get_list),
    path('get_rank/',get_rank),
    path('add_college/',add_college),
    path('edit/<int:college_id>/',edit_college),
    path('delete/<int:college_id>/',delete_college),
]
