# Generated by Django 3.2.23 on 2024-02-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_alter_question_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='participationapplicationfestival',
            name='pseudonym',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Псевдоним'),
        ),
    ]
