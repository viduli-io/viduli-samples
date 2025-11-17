from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Admin interface for custom User model."""

    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "date_joined",
    ]
    search_fields = ["username", "email", "first_name", "last_name"]
