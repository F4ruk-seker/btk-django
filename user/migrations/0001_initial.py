# Generated by Django 5.0.2 on 2024-03-09 08:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_pic', models.ImageField(default='/user/profile_pics/default.png', upload_to='user/profile_pics/')),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
