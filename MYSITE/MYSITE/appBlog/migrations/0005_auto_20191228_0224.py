# Generated by Django 2.2 on 2019-12-28 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0004_auto_20191227_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default-slug', unique=True),
        ),
    ]
