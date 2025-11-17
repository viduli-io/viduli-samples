from adrf.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from knox.auth import TokenAuthentication
from django.shortcuts import aget_object_or_404
from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    """Async viewset for Comment CRUD operations, nested under posts."""

    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter comments by post_id from URL."""
        post_id = self.kwargs.get("post_pk")
        return Comment.objects.filter(post_id=post_id).select_related("author", "post")

    async def perform_create(self, serializer):
        """Save the comment with the current user as author and the post from URL."""
        post_id = self.kwargs.get("post_pk")
        try:
            post = await aget_object_or_404(Post, pk=post_id)
            await serializer.asave(post=post)
        except Exception as e:
            raise NotFound(f"Post with id {post_id} not found")

    async def perform_update(self, serializer):
        """Update the comment."""
        await serializer.asave()
