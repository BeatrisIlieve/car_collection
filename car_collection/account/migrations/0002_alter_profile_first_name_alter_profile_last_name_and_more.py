# Generated by Django 4.2.4 on 2023-09-13 13:21

import car_collection.account.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), car_collection.account.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), car_collection.account.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
