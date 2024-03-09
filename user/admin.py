from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = 'user_name', 'address', 'city', 'country', 'phone_number', 'image_tag'

