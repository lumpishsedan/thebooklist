# pages/views.py
from django.views.generic import ListView
from django.views.generic import View
#from django.views.generic import TemplateView
#from django.views.generic.edit import CreateView # new
from django.shortcuts import render
from .forms import BookForm

from .models import Book
class HomePageView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new


class BookCreateView(View):
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'about.html', {'form': form})

    def get(self, request):
        form = BookForm()
        return render(request, 'about.html', {'form': form})
