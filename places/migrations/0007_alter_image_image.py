# Generated by Django 4.1.3 on 2022-11-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Картинка'),
        ),
    ]