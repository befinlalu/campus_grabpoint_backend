from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "full_name", "phone_number", "is_verified", "is_staff", "is_active")  # Add is_verified here
    search_fields = ("username", "email", "phone_number", "full_name")  # Add is_verified to search if needed
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("email", "phone_number", "full_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "is_verified")}),  # Add is_verified here
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "phone_number", "full_name", "password1", "password2"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
