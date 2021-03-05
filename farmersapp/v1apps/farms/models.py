from django.db import models
from django.utils.translation import ugettext_lazy as _
import jsonfield

from v1apps.user.models import User
# Create your models here.


class Farm(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=True)
    area = models.CharField(_('area'), max_length=30, blank=True)
    village = models.CharField(_('village'), max_length=30, blank=True)
    district = models.CharField(_('district'), max_length=30, blank=True)
    acres = models.IntegerField(_('acres'), max_length=30, blank=True)
    whether = models.CharField(_('whether'), max_length=30, blank=True)
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    geo = jsonfield.JSONField()
    soil_health = models.IntegerField(_('Soil Health'), blank=True)

    def __str__(self):
        return self.name


# class GeoTag(models.Model):
#     user = models.ForeignKey(User, related_name='user_geo_tag', on_delete=models.CASCADE)
#     farm = models.ForeignKey(Farm, related_name='farm_geo_tag', on_delete=models.CASCADE)
#     loc_lat_long = jsonfield.JSONField()
