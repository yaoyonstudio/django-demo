from django.contrib import admin
from .models import Post

# Register your models here.
from .models import Config, Menu, Slide, Featured, Page, Post, Cate
admin.site.register(Config)
admin.site.register(Menu)
admin.site.register(Slide)
admin.site.register(Featured)
admin.site.register(Page)
admin.site.register(Cate)
# admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['post_modified']
    fields = ['post_title', 'post_author', 'cate', 'post_status', 'post_recommend', 'post_date', 'post_excerpt', 'post_content']

admin.site.register(Post, PostAdmin)

