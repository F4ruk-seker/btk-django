# Generated by Django 5.0.2 on 2024-03-02 11:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_settings_aboutus_remove_settings_contactus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='aboutus',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='contactus',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='references',
            field=ckeditor.fields.RichTextField(blank=True, default=None, null=True),
        ),
    ]