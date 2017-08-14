from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Slide(models.Model):
    slide_title = models.CharField(max_length=250)
    slide_src = models.FileField(upload_to='slides/%Y/%m/%d/')
    slide_link = models.CharField(max_length=250)

    def __str__(self):
        return self.slide_title

class Featured(models.Model):
    featured_title = models.CharField(max_length=250)
    types = (
        (1, '特色项目'),
        (2, '特色跨栏'),
    )
    featured_type = models.IntegerField(
        choices=types,
        default=1
    )
    featured_src = models.FileField(upload_to='featured/%Y/%m/%d/')
    featured_desc = models.CharField(max_length=250)
    featured_link = models.CharField(max_length=250)

    def __str__(self):
        return self.featured_title

    # def __repr__(self):
    #     return self

class Page(models.Model):
    page_title = models.CharField(max_length=200)
    page_name = models.CharField(max_length=200)
    page_author = models.ForeignKey('auth.User')
    page_status = models.BooleanField('page_status', default=True)
    page_date = models.DateTimeField(default=timezone.now)
    page_modified = models.DateTimeField(default=timezone.now)
    page_excerpt = models.TextField()
    page_content = RichTextUploadingField()

    def __str__(self):
        return self.page_title


class Cate(models.Model):
    cate_title = models.CharField(max_length=100)
    cate_name = models.CharField(max_length=100, blank=True)
    cate_desc = models.CharField(max_length=100)
    cate_date = models.DateTimeField(default=timezone.now)
    cate_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cate_title


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_name = models.CharField(max_length=200)
    post_author = models.ForeignKey('auth.User')
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE)
    post_status = models.BooleanField('page_status', default=True)
    post_date = models.DateTimeField(default=timezone.now)
    post_modified = models.DateTimeField(default=timezone.now)
    post_excerpt = models.TextField()
    post_content = RichTextUploadingField()

    def __str__(self):
        return self.post_title
