from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    features = []
    places = Place.objects.all()
    for place in places:

        features_data = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'detailsUrl': reverse('places', args=(place.id, )),
                }
            }
        features.append(features_data)

    geo_places = {
        'type': 'FeatureCollection',
        'features': features
    }

    context = {
        'GeoJSON': geo_places,
    }

    return render(request, 'index.html', context=context)


def get_place_detail(request, place_id):
    place_details = get_object_or_404(Place, id=place_id)
    images = place_details.images.all()
    title = place_details.title
    imgs = [img.photo.url for img in images]
    description_short = place_details.description_short
    description_long = place_details.description_long
    coordinates = [place_details.lat, place_details.lng]

    place_descriptions = {

            'title': title,
            'imgs': imgs,
            'description_short': description_short,
            'description_long': description_long,
            'coordinates': coordinates,

            }
    return JsonResponse(place_descriptions, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})

