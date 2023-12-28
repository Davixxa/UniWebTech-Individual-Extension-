# Generated by Django 5.0 on 2023-12-26 23:32

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_review_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='cover',
            field=models.ImageField(upload_to='covers/%Y/%m/%d', verbose_name='cover'),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, max_length=2000, validators=[django.core.validators.MaxLengthValidator(2000)]),
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.developer'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.genre'),
        ),
    ]
