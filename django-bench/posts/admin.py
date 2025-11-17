from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin interface for Post model."""

    list_display = ["id", "author", "title_preview", "created_at", "updated_at"]
    list_filter = ["created_at", "author"]
    search_fields = ["title", "author__username"]
    readonly_fields = ["created_at", "updated_at"]
    date_hierarchy = "created_at"

    def title_preview(self, obj):
        """Show preview of post text."""
        return obj.title[:50] + "..." if len(obj.title) > 50 else obj.title

    title_preview.short_description = "Title"
