from django.shortcuts import render
from .models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse


# Create your views here.
def creating_place_params(request):
    features = []
    places = Place.objects.all()
    for place in places:
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_by_id', args=[place.id])
            }
        })
    context = {
        'places_geojson': {
            'type': 'FeatureCollection',
            'features': features
        }
    }
    return render(request, 'index.html', context)


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_details = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }
    return JsonResponse(place_details, json_dumps_params={'ensure_ascii': False})
