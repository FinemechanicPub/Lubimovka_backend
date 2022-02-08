# Generated by Django 3.2.11 on 2022-02-08 09:14

import apps.library.validators
import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_play_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='someslug', verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='play',
            name='city',
            field=models.CharField(blank=True, max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='play',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, validators=[apps.library.validators.year_validator], verbose_name='Год написания пьесы'),
        ),
    ]
