# blog/models.py
from django.db import models
from django.urls import reverse # new

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('about')
