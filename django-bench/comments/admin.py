from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for Comment model."""

    list_display = [
        "id",
        "author",
        "post",
        "text_preview",
        "created_at",
        "updated_at",
    ]
    list_filter = ["created_at", "author", "post"]
    search_fields = ["text", "author__username", "post__text"]
    readonly_fields = ["created_at", "updated_at"]
    date_hierarchy = "created_at"

    def text_preview(self, obj):
        """Show preview of comment text."""
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text

    text_preview.short_description = "Text"
