Note that with templates we dont work with functions(def) but classes


# pages/views.py
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'
