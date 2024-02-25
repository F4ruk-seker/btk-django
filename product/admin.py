from django.contrib import admin
from .models import Category, Product, Images


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title', 'status'
    list_filter = 'status', 'parent'
    prepopulated_fields = {'slug': ('title',)}
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
    #


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title', 'status', 'image_tag'
    list_filter = 'status', 'category'
    readonly_fields = 'image_tag',
    # inlines = ProductImageInline
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = 'title', 'image_tag'
    readonly_fields = 'image_tag',

