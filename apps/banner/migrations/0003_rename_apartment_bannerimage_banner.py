# Generated by Django 4.2.2 on 2023-07-03 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_bannerimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bannerimage',
            old_name='apartment',
            new_name='banner',
        ),
    ]
