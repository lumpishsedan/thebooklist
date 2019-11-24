Since app_views were updated with class (than function) we make appropriate change to app_urls

# pages/urls.py
from django.urls import path
from .views import HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
