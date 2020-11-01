from django.urls import path
 
from . import views,testdb
 
urlpatterns = [
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb),
]