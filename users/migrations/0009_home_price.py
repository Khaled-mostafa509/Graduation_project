# Generated by Django 4.0 on 2022-01-03 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_home_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='price',
            field=models.TextField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
