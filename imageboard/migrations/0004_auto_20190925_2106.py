# Generated by Django 2.1.8 on 2019-09-25 12:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imageboard', '0003_auto_20190925_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageboard',
            name='like_posts',
        ),
        migrations.AddField(
            model_name='imageboard',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
