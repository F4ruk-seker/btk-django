# Generated by Django 5.0.2 on 2024-03-02 13:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
    ]