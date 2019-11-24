repeat views.py / app_urls.py / project_urls.py

=========================================================
# blog/views.py
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    
=========================================================
# blog/urls.py
from django.urls import path
from .views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]


=========================================================
# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # new
]

