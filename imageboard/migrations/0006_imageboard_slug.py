# Generated by Django 2.1.8 on 2019-09-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageboard', '0005_auto_20190925_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageboard',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
