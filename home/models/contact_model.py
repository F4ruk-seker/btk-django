from django.db import models


class ContactModel(models.Model):
    STATUS: tuple = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Close', 'Close'),
    )
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    ip = models.CharField(max_length=15, blank=True)
    notes = models.TextField(blank=True)
    messages = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


