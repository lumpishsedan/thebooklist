# helloworld_project/urls.py

Code 1 is updated to Code 2
#########################################

Code 1

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
#########################################

Code 2

from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
