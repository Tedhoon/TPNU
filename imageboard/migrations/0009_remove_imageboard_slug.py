# Generated by Django 2.1.8 on 2019-09-25 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageboard', '0008_imageboard_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageboard',
            name='slug',
        ),
    ]
