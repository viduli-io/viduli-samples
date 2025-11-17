from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model with validation."""

    text = serializers.CharField(
        required=True,
        allow_blank=False,
        trim_whitespace=True,
        min_length=1,
        max_length=10_000,
    )

    class Meta:
        model = Comment
        fields = ["id", "text", "post", "author", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "post", "created_at", "updated_at"]
