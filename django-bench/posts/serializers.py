from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model with validation."""

    title = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        min_length=1,
        max_length=255,
    )
    body = serializers.TextField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        min_length=1,
        max_length=10_000,
    )

    class Meta:
        model = Post
        fields = ["id", "title", "body", "author", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "created_at", "updated_at"]
