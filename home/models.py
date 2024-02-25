from django.db import models


class Settings(models.Model):
    STATUS = (('True', 'True'), ('False', 'False'),)
    title = models.CharField(blank=True, max_length=150)
    keyword = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    company = models.CharField(blank=True, max_length=55)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtpassword = models.CharField(blank=True, max_length=10)
    smtpport = models.IntegerField()
    status = models.CharField(blank=True, max_length=10, choices=STATUS, default='True')

    icon = models.ImageField(upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField()
    contactus = models.TextField()
    references = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
