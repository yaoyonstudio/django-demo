from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Config(models.Model):
    config_key = models.CharField(max_length=250)
    config_value = models.CharField(max_length=250)

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = '配置管理'

    def __str__(self):
        return self.config_value

class Menu(models.Model):
    menu_title = models.CharField(max_length=250)
    menu_link = models.CharField(max_length=250)
    menu_src = models.FileField(upload_to='icon/%Y/%m/%d/', blank=True)
    menu_desc = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = '菜单管理'

    def __str__(self):
        return self.menu_title

class Slide(models.Model):
    slide_title = models.CharField(max_length=250)
    slide_src = models.FileField(upload_to='slides/%Y/%m/%d/')
    slide_link = models.CharField(max_length=250)

    class Meta:
        verbose_name = '滑动图'
        verbose_name_plural = '滑动图'

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

    class Meta:
        verbose_name = '特色栏目'
        verbose_name_plural = '特色栏目'

    def __str__(self):
        return self.featured_title

    # def __repr__(self):
    #     return self

class Page(models.Model):
    page_title = models.CharField(max_length=200)
    page_name = models.CharField(max_length=200)
    page_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    page_status = models.BooleanField('page_status', default=True)
    page_date = models.DateTimeField(default=timezone.now)
    page_modified = models.DateTimeField(default=timezone.now)
    page_excerpt = models.TextField()
    page_content = RichTextUploadingField()

    class Meta:
        verbose_name = '页面'
        verbose_name_plural = '管理页面'

    def __str__(self):
        return self.page_title


class Cate(models.Model):
    cate_title = models.CharField(max_length=100)
    cate_name = models.CharField(max_length=100, blank=True)
    cate_desc = models.CharField(max_length=100)
    cate_date = models.DateTimeField(default=timezone.now)
    cate_modified = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = '管理文章类别'

    def __str__(self):
        return self.cate_title


class Post(models.Model):
    post_title = models.CharField('标题', max_length=200)
    post_author = models.ForeignKey('auth.User', verbose_name='作者', on_delete=models.CASCADE)
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE, verbose_name='类别')
    post_status = models.BooleanField('是否发布', default=True)
    post_recommend = models.BooleanField('是否推荐', default=False)
    post_date = models.DateTimeField('发布时间', default=timezone.now)
    post_modified = models.DateTimeField('修改时间', default=timezone.now)
    post_excerpt = models.TextField('摘要')
    post_content = RichTextUploadingField('内容')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '管理文章'

    def __str__(self):
        return self.post_title

