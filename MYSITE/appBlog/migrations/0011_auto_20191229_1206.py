# Generated by Django 2.2 on 2019-12-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0010_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
