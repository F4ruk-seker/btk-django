# Generated by Django 5.0.2 on 2024-03-02 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_settings_aboutus_alter_settings_contactus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='aboutus',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='contactus',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='references',
        ),
    ]
