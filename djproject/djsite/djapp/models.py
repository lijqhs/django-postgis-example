# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# Create your models here.

class Restaurant(models.Model):
    CHOICES_CUISINE_TYPE = [
        ('Asian food', 'Asian food'),
        ('European cuisine', 'European cuisine'),
        ('Cuisine of the Americas', 'Cuisine of the Americas'),
        ('African cuisine', 'African cuisine'),
    ]
    brand = models.CharField(verbose_name='Brand Name *', max_length=256)
    cuisine_type = models.CharField(max_length=128, choices=CHOICES_CUISINE_TYPE, null=True, blank=True)
    address = models.CharField(verbose_name='Address *', max_length=256)
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    location = models.PointField(srid=4326, null=True, blank=True)

    def save(self, *args, **kwargs):        
        if self.lon and self.lat:
            self.location = Point(self.lon, self.lat, srid=4326)
        super().save(*args, **kwargs)