# Generated by Django 4.2.2 on 2023-06-13 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_apartment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='price_from',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='price_until',
        ),
    ]
