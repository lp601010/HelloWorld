from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('add_emp/', views.add_emp),
]