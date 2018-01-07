from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # 常规urls
    # re_path(r'^post/$', views.PostList),
    # re_path(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail),

    # 基于类的urls
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),

    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),

    path('api-auth/', include('rest_framework.urls')),
]

# 加上这个可以使用接口json后缀的形式访问api, 如：
# http://127.0.0.1:8000/api/post.json
urlpatterns = format_suffix_patterns(urlpatterns)

