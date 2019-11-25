below there are two concepts that are extremely useful to understand
get_absolute_url and reverse
these are used to specify where to send the user after successfully submitting the form.
reverse of post_detail means that using the name post_detail we are fetching the url linked
with post_detail name in the urls.py 
this is the url patterns
path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
note that url has <int:pk> 
that is in the reverse you also need to specify the argument of primary key. 
we provide that using the code args=[str(self.id)]
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# blog/models.py
from django.db import models
from django.urls import reverse # new

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    )
    body = models.TextField()
    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])