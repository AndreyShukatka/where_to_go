from django.core.management.base import BaseCommand
import requests
from django.core.files.base import ContentFile

from ...models import Place, Image


class Command(BaseCommand):
    help = 'Заполнение базы данных по ссылке на джейсон'

    def add_arguments(self, parser):
        parser.add_argument('url',
                            type=str,
                            default=False,
                            help='url адрес джейсона'
                            )

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        place_params = response.json()
        title = place_params.get('title')
        description_short = place_params.get('description_short', '')
        description_long = place_params.get('description_long', '')
        lng = place_params.get('coordinates').get('lng')
        lat = place_params.get('coordinates').get('lat')
        images = place_params.get('imgs')

        place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                'description_short': description_short,
                'description_long': description_long,
                'lat': lat,
                'lng': lng,
            }
        )
        if created:
            self.download_images(images, place)

    def download_images(self, images, place):
        for number, image in enumerate(images):
            image_response = requests.get(image)
            image_response.raise_for_status()
            content_file = ContentFile(
                image_response.content,
                name=f'{place}{number}.jpg'
            )
            Image.objects.create(
                place=place,
                image=content_file,
                position=number
            )
