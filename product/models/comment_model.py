from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Comment(models.Model):
    STATUS: tuple = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    comment = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default=0, blank=True)
    ip = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject