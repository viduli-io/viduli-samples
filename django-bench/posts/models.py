from django.conf import settings
from django.db import models


class Post(models.Model):
    """Post model with text content and author."""

    title = models.CharField(max_length=255, help_text="Title of the post")
    body = models.TextField(max_length=10_000, help_text="Content of the post")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        help_text="Author of the post",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return f"Post by {self.author.username}: {self.title}"
