from django.conf import settings
from django.db import models


class Comment(models.Model):
    """Comment model with text content, post reference, and author."""

    text = models.TextField(help_text="Content of the comment")
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="comments",
        help_text="Post this comment belongs to",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        help_text="Author of the comment",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"
