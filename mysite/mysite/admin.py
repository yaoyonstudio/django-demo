from django.contrib import admin

# Register your models here.
from .models import Slide, Featured, Page, Post, Cate
admin.site.register(Slide)
admin.site.register(Featured)
admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Cate)