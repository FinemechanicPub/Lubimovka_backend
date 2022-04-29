# Generated by Django 3.2.12 on 2022-04-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0004_alter_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('PERFORMANCE', 'Спектакль'), ('MASTERCLASS', 'Мастер-класс'), ('READING', 'Читка')], help_text='Выберите тип события', max_length=50, verbose_name='Тип события'),
        ),
    ]
