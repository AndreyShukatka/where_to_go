# Generated by Django 4.1.3 on 2022-11-20 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description_short', models.CharField(max_length=350, verbose_name='Краткое описание')),
                ('lat', models.FloatField(null=True, verbose_name='Точка координат lat')),
                ('lng', models.FloatField(null=True, verbose_name='Точка координат lng')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Картинка')),
                ('position', models.IntegerField(default=0, verbose_name='позиция')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='places.place', verbose_name='Место')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
