# Generated by Django 3.2.7 on 2021-10-18 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_infoblock_mainsettings_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ['text_order'], 'verbose_name': 'Текст', 'verbose_name_plural': 'Тексты'},
        ),
        migrations.RenameField(
            model_name='text',
            old_name='order',
            new_name='text_order',
        ),
    ]
