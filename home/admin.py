from django.contrib import admin
from . import models


admin.site.register(models.Settings)
# admin.site.register(models.ContactModel)


@admin.register(models.ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display: list = 'subject', 'name', 'email'
    list_filter: list = 'status',
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    readonly_fields: list = 'messages',
    # search_fields = ['']
    # ordering = ['']

