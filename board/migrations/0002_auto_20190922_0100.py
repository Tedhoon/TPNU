# Generated by Django 2.1.8 on 2019-09-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeboard',
            name='title',
            field=models.TextField(max_length=200),
        ),
    ]
