checkout the function HomePageView 
we introduce the filter here 

# pages/views.py
from django.views.generic import TemplateView, DetailView, ListView # new
from django.views.generic.edit import CreateView # new

from django.shortcuts import render

from .models import Post


class SelectView(TemplateView):
    template_name = 'select.html'

class PostView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class PostDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'


def HomePageView(request):
    key2select = Post.objects.filter(keyone=2)
    return render(request, 'home.html', {
        'key2select': key2select,
    })
