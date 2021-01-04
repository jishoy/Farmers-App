from django.db import models
from django.utils.translation import ugettext_lazy as _

from v1apps.user.models import User
# Create your models here.


class Farm(models.Model):
    area = models.CharField(_('area'), max_length=30, blank=True)
    village = models.CharField(_('village'), max_length=30, blank=True)
    district = models.CharField(_('district'), max_length=30, blank=True)
    whether = models.CharField(_('whether'), max_length=30, blank=True)
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.area