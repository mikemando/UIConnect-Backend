import cloudinary
import cloudinary.uploader
import cloudinary.models

from django.db import models
from django.conf import settings


class Store(models.Model):
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="stores")
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = cloudinary.models.CloudinaryField("store_logo", blank=True, null=True)
    category = models.CharField(max_length=255)
    theme_color = models.CharField(max_length=7, blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class StoreItem(models.Model):
    store = models.ForeignKey("Store", on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = cloudinary.models.CloudinaryField("store_items", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name