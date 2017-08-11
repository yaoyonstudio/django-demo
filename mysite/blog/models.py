from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_publish = models.DateTimeField('date published')

