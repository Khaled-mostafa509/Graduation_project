# Generated by Django 4.0 on 2022-01-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_home_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.ImageField(default=1, upload_to='Home/'),
            preserve_default=False,
        ),
    ]
