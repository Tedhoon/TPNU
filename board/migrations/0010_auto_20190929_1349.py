# Generated by Django 2.1.8 on 2019-09-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20190925_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeboard',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]