# Generated by Django 3.2.13 on 2022-07-20 12:01

import apps.content_pages.utilities
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0033_alter_play_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='url_download_from',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на скачивание пьесы'),
        ),
        migrations.AlterField(
            model_name='play',
            name='url_download',
            field=models.FileField(blank=True, help_text="Файл пьесы должен быть в одном из следующих форматов: ('doc', 'docx', 'txt', 'odt', 'pdf')", max_length=200, null=True, upload_to=apps.content_pages.utilities.path_by_media_and_class_name, validators=[django.core.validators.FileExtensionValidator(('doc', 'docx', 'txt', 'odt', 'pdf'))], verbose_name='Текст пьесы'),
        ),
        migrations.AddConstraint(
            model_name='play',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('url_download__isnull', True), ('url_download_from__isnull', False)), models.Q(('url_download__isnull', False), ('url_download_from__isnull', True)), _connector='OR'), name='play_file_download_or_url_download_from'),
        ),
    ]
