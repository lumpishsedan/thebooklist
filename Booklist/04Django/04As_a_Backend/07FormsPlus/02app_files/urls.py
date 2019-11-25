# booklist/urls.py
from django.urls import path
from .views import HomePageView, BookCreateView # new
urlpatterns = [
    path('about/', BookCreateView.as_view(), name='about'), # new
    path('', HomePageView.as_view(), name='home'),

]
