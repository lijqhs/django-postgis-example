import logging
from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Restaurant

logger = logging.getLogger(__name__)

def search(request):
    if request.method == 'GET':
        lon = request.GET.get('lon')
        lat = request.GET.get('lat')
        radius = request.GET.get('distance', 10000) # meters
        logger.debug(f'{lon=}, {lat=}, {radius=}')

        if lon and lat:
            input_location = Point(float(lon), float(lat), srid=4326)
            results = Restaurant.objects.annotate(
                distance=Distance('location', input_location)).filter(
                    distance__lte=radius).order_by('distance')
        else:
            results = Restaurant.objects.all()

        return render(request, 'search.html', {'results': results})