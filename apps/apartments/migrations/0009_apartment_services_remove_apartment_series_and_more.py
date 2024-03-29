# Generated by Django 4.2.2 on 2023-08-08 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('apartments', '0008_apartment_phone_number_apartment_plot_weaving_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='services',
            field=models.ManyToManyField(blank=True, null=True, to='services.service'),
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='series',
        ),
        migrations.AddField(
            model_name='apartment',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.series'),
        ),
    ]
