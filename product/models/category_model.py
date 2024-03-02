from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    status = models.CharField(max_length=10, choices=STATUS)

    title = models.CharField(max_length=30)
    keyword = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self',
                            blank=True,
                            null=True,
                            default=None,
                            related_name='children',
                            on_delete=models.CASCADE
                            )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
