from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Category,Product

class CustomUserAdmin(UserAdmin):
    # Specify the fields to be displayed in the user list
    list_display = ('username', 'email', 'full_name', 'phone_number', 'is_verified', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'full_name', 'phone_number')  # Enable search by username, email, full name, and phone number
    ordering = ('username',)

    # Fields to be displayed when editing a user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_verified', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Fields to be displayed in the form to add/edit a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'full_name', 'phone_number', 'is_verified', 'is_active')
        }),
    )
    # Make sure to set this so the user model is editable through the admin interface
    filter_horizontal = ('groups', 'user_permissions',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Only display the name
    search_fields = ("name",)  # Allow searching by category name
    ordering = ("name",)  # Sort by name

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'price', 'available_quantity', 'sale_price', 'category')  # Customize displayed fields
    search_fields = ('name', 'category__name')  # Allow searching by product name and category name
    list_filter = ('category',)  # Filter products by category

admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
