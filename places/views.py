from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from places.models import Place


def index(request):
    places = {
        "type": "FeatureCollection",
        "features": []
    }

    place_data = Place.objects.all()
    for data in place_data:
        features_data = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": []
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "../static/places/moscow_legends.json"
                }
            }

        features_data['geometry']['coordinates'] = [data.lng, data.lat]
        features_data['properties']['title'] = data.title
        places["features"].append(features_data)

    data = {
        'places': places,
    }

    return render(request, 'index.html', context=data)


def place_detail(request, post_id):
    place_details = get_object_or_404(Place, id=post_id)
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

