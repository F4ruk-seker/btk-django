# Generated by Django 5.0.2 on 2024-03-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
