import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        help = 'Загружает данные в базу из json файла'

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
            title=response['title'],
            defaults={
                'description_short': response['description_short'],
                'description_long': response['description_long'],
                'lng': response['coordinates']['lng'],
                'lat': response['coordinates']['lat'],
            },
        )
        img_urls = response['imgs']
        for order, img_url in enumerate(img_urls):
            try:
                response = requests.get(img_url)
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                print('Сервер не доступен')
                exit()

            image = Image.objects.create(place_id=place.id, order=order)
            content = ContentFile(response.content)
            image.photo.save(name='image.jpg', content=content, save=True)
