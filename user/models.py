from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to='user/profile_pics/', default='/user/profile_pics/default.png')
    phone_number = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'Profile ({self.user})'

    @property
    def user_name(self):
        return f'{self.user.first_name} {self.user.last_name}[{self.user.username}]'

    def image_tag(self):
        if self.profile_pic:
            return mark_safe(f'<img src="{self.profile_pic.url}" width="100%" height="100" style="object-fit:center"')

    image_tag.short_description = 'Image'
