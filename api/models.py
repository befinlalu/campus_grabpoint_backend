from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False) 

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name of the category

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name
    short_description = models.CharField(max_length=255)  # Short description
    full_description = models.TextField()  # Full description
    image = models.ImageField(upload_to='product_images/')  # Product image
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price
    available_quantity = models.PositiveIntegerField()  # Available quantity
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Sale price (optional)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # Category
    
    def __str__(self):
        return self.name