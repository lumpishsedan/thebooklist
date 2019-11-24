we will now work on views.
note that last time we worked on views, we imported
templateview
this time since we want a list out of database
we will import listview and models

# posts/views.py
from django.views.generic import ListView
from .models import Post
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new

