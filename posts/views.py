from django.contrib.auth import get_user_model
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostList(generics.ListCreateAPIView):
    # View-based permission are good for small aps, but its better to use project-based ones
    # permission_classes = (permissions.IsAuthenticated, )  # View-based permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # View-based permission are good for small aps, but its better to use project-based ones
    # permission_classes = (permissions.IsAuthenticated, )  # View-based permissions
    # If we need special rules, we do it this way
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer