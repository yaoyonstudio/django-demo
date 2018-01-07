from rest_framework import serializers

from django.contrib.auth.models import User
from mysite.models import Post

class UserSerializer(serializers.ModelSerializer):
  posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
  class Meta:
    model = User
    fields = ('id', 'username', 'posts')

class postSerializer(serializers.ModelSerializer):
  post_author_name = serializers.ReadOnlyField(source='post_author.username')
  class Meta:
    model = Post
    # 指定api返回模型字段
    # fields=('post_title', 'post_content')
    # 所有字段
    fields='__all__'

