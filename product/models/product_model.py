from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


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

    def image_tag(self):
        return mark_safe('<img src="{}" width="50px" height="50px" style="object-fit:cover;">'.format(self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title
