# Generated by Django 3.2 on 2021-04-29 09:31

import django.core.validators
from django.db import migrations, models
import listings.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210429_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='date',
            field=models.DateField(blank=True, default=None, null=True, validators=[listings.models.Listing.validate_date]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]