# Generated by Django 2.2 on 2019-12-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0013_auto_20191230_1110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated', '-pk', '-timestamp']},
        ),
    ]
