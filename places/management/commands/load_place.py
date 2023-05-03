import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает данные в базу по ссылке json файла'

    def add_arguments(self, parser):
        parser.add_argument('json_url', help='Введите ссылку на Json файл')

    def handle(self, *args, **options):
        try:
            response = requests.get(options['json_url'])
            response.raise_for_status()
            payload = response.json()
        except requests.exceptions.HTTPError:
            print('Сервер не доступен')
            exit()

        place, created = Place.objects.get_or_create(
            title=payload['title'],
            lng=payload['coordinates']['lng'],
            lat=payload['coordinates']['lat'],
            defaults={
                'description_short': payload.get('description_short', ''),
                'description_long': payload.get('description_long', ''),
            }
        )
        if created:
            img_urls = payload.get('imgs', [])
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
