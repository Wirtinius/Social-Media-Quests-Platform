from rest_framework.generics import ListAPIView
from .serializers import PostSerializer
from .models import Post

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer