# Generated by Django 2.1.8 on 2019-09-25 11:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imageboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageboard',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='imageboard',
            name='image',
            field=models.ImageField(upload_to='imageboard/'),
        ),
    ]
