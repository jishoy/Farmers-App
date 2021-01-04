from django.db import models
from django.utils.translation import ugettext_lazy as _

from v1apps.user.models import User
from v1apps.farms.models import Farm
# Create your models here.


class Crop(models.Model):
    crop_name = models.CharField(_('Crop Name'), max_length=30, blank=True)
    exp_price = models.IntegerField(_('Expected Price'), blank=True)
    exp_yield = models.CharField(_('Expected Yield'), max_length=30, blank=True)
    exp_harvest_date = models.DateField(_('Expected Harvest Date'), blank=True)
    crop_images = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    user = models.ForeignKey(User, related_name='user_crop', on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, related_name='farm_crop', on_delete=models.CASCADE)
    sell_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.crop_name
