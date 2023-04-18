import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает данные в базу из json файла'

    def add_arguments(self, parser):
        parser.add_argument('json_url', help='Введите ссылку на Json файл')

    def handle(self, *args, **options):
        try:
            response = requests.get(options['json_url'])
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError:
            print('Сервер не доступен')
            exit()

        place, created = Place.objects.get_or_create(
            title= response['title'],
            lng=response['coordinates']['lng'],
            lat=response['coordinates']['lat'],
            defaults={
                'description_short': response.get('description_short', ''),
                'description_long': response.get('description_long', ''),
            }
        )
        if created:
            img_urls = response.get('imgs', [])
            for order, img_url in enumerate(img_urls):
                try:
                    response = requests.get(img_url)
                    response.raise_for_status()
                except requests.exceptions.HTTPError:
                    print('Сервер не доступен')
                    exit()

                Image.objects.create(
                    place_id=place.id,
                    order=order,
                    photo=ContentFile(response.content, 'image.jpg')
                )
