from django.urls import path,re_path
from . import views,testdb,search,search2

from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb),
    re_path(r'^search-form$', search.search_form),
    re_path(r'^search$', search.search),
    re_path(r'^search-post$', search2.search_post),
    url(r'^admin/', admin.site.urls),
]