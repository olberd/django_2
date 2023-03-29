from django.shortcuts import render

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
