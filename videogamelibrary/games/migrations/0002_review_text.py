# Generated by Django 5.0 on 2023-12-26 20:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, max_length=1000, validators=[django.core.validators.MaxLengthValidator(1000)]),
        ),
    ]