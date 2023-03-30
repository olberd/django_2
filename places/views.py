from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    places = Place.objects.all()
    for place in places:

        features_data = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "detailsUrl": reverse('places', args=(place.id, )),
                }
            }

        geo_json["features"].append(features_data)

    context = {
        'GeoJSON': geo_json,
    }

    return render(request, 'index.html', context=context)


def place_detail(request, place_id):
    place_details = get_object_or_404(Place, id=place_id)
    images = place_details.images.all()
    title = place_details.title
    imgs = [img.photo.url for img in images]
    description_short = place_details.description_shot
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

