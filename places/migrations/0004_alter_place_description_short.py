# Generated by Django 4.1.3 on 2022-11-21 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
    ]
