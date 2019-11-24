Just Create a new project called
blog_project
and new app call blog
update settings.py
make project admin ready
and then -------- >

# blog/models.py
from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    )
    body = models.TextField()
    def __str__(self):
        return self.title
