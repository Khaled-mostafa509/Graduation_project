# Generated by Django 4.0 on 2022-01-01 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_home_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='image',
        ),
    ]