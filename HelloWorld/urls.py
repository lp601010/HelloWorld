from django.urls import path,re_path
# from django.conf.urls import url
from . import views,testdb,search,search2
 
urlpatterns = [
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb),
    re_path(r'^search-form$', search.search_form),
    re_path(r'^search$', search.search),
    re_path(r'^search-post$', search2.search_post),
]