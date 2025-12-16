from django.db import models
from django.urls import reverse


class Product(models.Model):
    ICON_CHOICES = [
        ("mild", "Mild"),
        ("spicy", "Spicy"),
        ("fresh", "Fresh"),
        ("premium", "Premium"),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    short_description = models.CharField(max_length=200)
    description = models.TextField()

    icon_type = models.CharField(
        max_length=10,
        choices=ICON_CHOICES,
        blank=True,
        null=True,
    )

    image = models.ImageField(upload_to="products/", blank=True, null=True)

    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])
