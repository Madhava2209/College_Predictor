from django.contrib import admin
from django.urls import path
from College_Predictor.views import *

urlpatterns = [
    path('home/',home),
    path('create/',add_college),
    path('all_college/',all_college),
    path('get_list/',get_list),
    path('get_rank/',get_rank),
    path('add_college/',add_college),
    path('edit/<int:college_id>/',edit_college),
    path('delete/<int:college_id>/',delete_college),
]
