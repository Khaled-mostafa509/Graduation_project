# Generated by Django 4.0 on 2022-01-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_home_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(upload_to='media_files/'),
        ),
    ]
