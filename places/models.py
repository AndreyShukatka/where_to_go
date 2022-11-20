from django.db import models
# from tinymce.models import HTMLField


class Place(models.Model):
    objects = None
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.CharField(max_length=350, verbose_name='Краткое описание')
    # description_long = HTMLField(verbose_name='Полное описание')
    lat = models.FloatField(null=True, verbose_name='Точка координат lat')
    lng = models.FloatField(null=True, verbose_name='Точка координат lng')

    def __str__(self):
        return self.title


class Image(models.Model):
    objects = None
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='image'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        blank=True,
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
