# Generated by Django 4.0.4 on 2022-05-24 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_remove_city_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.country'),
        ),
    ]