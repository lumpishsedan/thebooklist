repeat the step at django as backend > part 1 > 2nd point

# blog/admin.py
from django.contrib import admin
from .models import Post
admin.site.register(Post)