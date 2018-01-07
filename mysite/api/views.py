from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions

from mysite.models import Post
from .serializers import postSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly

# Create your views here.

def index(request):
  return HttpResponse("api app")

# 定义api视图的四种不同方法：
# 第一种：常规方式
# 第二种：REST framework @api_view装饰器
# 第三种：REST framework 基于类的APIView
# 第四种：REST framework 泛型

# ####################################################

# 第一种：使用常规的django视图方法
# url模式：
# urlpatterns = [
#   re_path(r'^post/$', views.PostList),
#   re_path(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail),
# ]

# 同时，使用原生的HttpResponse和JsonResponse用于数据输出，要使用JSONParser转换输入格式
'''
@csrf_exempt
def PostList(request):
  if (request.method == 'GET'):
    posts = Post.objects.all()
    serializer = postSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = postSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


# 第一种：使用常规的django视图方法
@csrf_exempt
def PostDetail(request, pk):
  try:
    post = Post.objects.get(pk=pk)
  except Post.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = postSerializer(post)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
      data = JSONParser().parse(request)
      serializer = postSerializer(post, data=data)
      if serializer.is_valid():
          serializer.save()
          return JsonResponse(serializer.data)
      return JsonResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
      post.delete()
      return HttpResponse(status=204)
'''

# ####################################################

# 第二种：使用REST framework 的@api_view装饰器封装，同时使用REST framework的Response返回数据
# url模式：
# urlpatterns = [
#   re_path(r'^post/$', views.PostList),
#   re_path(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail),
# ]
'''
@api_view(['GET', 'POST'])
def PostList(request, format=None):
  if request.method == 'GET':
    posts = Post.objects.all()
    serializer = postSerializer(posts, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = postSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 第二种：使用REST framework 的@api_view装饰器封装，同时使用REST framework的Response返回数据
@api_view(['GET', 'PUT', 'DELETE'])
def PostDetail(request, pk, format=None):
  try:
    post = Post.objects.get(pk=pk)
  except Post.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = postSerializer(post)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = postSerializer(post, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
'''

# ####################################################

# 第三种: 使用'基于类'的PostList方法
# url模式：
# urlpatterns = [
#   path('post/', views.PostList.as_view()),
#   path('post/<int:pk>/', views.PostDetail.as_view()),
# ]
'''
class PostList(APIView):
  def get(self, request, format=None):
    posts = Post.objects.all()
    serializer = postSerializer(posts, many = True)
    return Response(serializer.data)
  
  def post(self, request, format=None):
    serializer = postSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 第三种: 使用'基于类'的PostDetail方法
class PostDetail(APIView):
  def get_object(self, pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    post = self.get_object(pk)
    serializer = postSerializer(post)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    post = self.get_object(pk)
    serializer = postSerializer(post, data=request.data)
    if (serializer.is_valid()):
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    post = self.get_object(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
'''

# ####################################################

# 第四种: 使用'基于泛型'PostList，比前面的方法更加简便
# url模式：
# urlpatterns = [
#   path('post/', views.PostList.as_view()),
#   path('post/<int:pk>/', views.PostDetail.as_view()),
# ]
'''
class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = postSerializer

# 第四种: 使用'基于泛型'的PostDetail方法，比前面的方法更加简便
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = postSerializer
'''

# ####################################################

# 加入用户验证

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = postSerializer
  # 添加验证
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
  def perform_create(self, serializer):
    serializer.save(post_author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = postSerializer
  # 添加验证
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


