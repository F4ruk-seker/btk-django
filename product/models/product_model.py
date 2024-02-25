from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amount = models.IntegerField(default=0)
    details = models.TextField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
