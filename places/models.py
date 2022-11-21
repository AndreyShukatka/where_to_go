from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = HTMLField(blank=True, verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Точка координат lat')
    lng = models.FloatField(verbose_name='Точка координат lng')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='images'
    )
    position = models.IntegerField(
        default=0,
        verbose_name='позиция'
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
