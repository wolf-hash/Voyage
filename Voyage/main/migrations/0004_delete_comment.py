# Generated by Django 3.2 on 2021-05-01 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_comments_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
