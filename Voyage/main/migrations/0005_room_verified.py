# Generated by Django 3.2 on 2021-05-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_booking_adults'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
