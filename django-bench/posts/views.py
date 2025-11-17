from adrf.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """Async viewset for Post CRUD operations."""

    queryset = Post.objects.select_related("author").all()
    serializer_class = PostSerializer
