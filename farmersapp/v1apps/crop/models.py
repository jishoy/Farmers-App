from django.db import models
from django.utils.translation import ugettext_lazy as _

from v1apps.user.models import User
from v1apps.farms.models import Farm
# Create your models here.


class CropActivity(models.Model):
    crops = models.ForeignKey('Crop', default=None, on_delete=models.CASCADE)
    activity = models.TextField()
    images = models.FileField(upload_to='images/')
    date = models.DateField(_('Date'))

    def __str__(self):
        return self.crops.crop_name


class Crop(models.Model):
    crop_name = models.CharField(_('Crop Name'), max_length=30)
    acres = models.CharField(_('Acres'), max_length=30)
    exp_price = models.IntegerField(_('Expected Price'))
    total_expense = models.IntegerField(_('Total Expense'))
    fertilizer_expense = models.IntegerField(_('Fertilizer Expense'))
    seed_expense = models.IntegerField(_('Seed Expense'))
    machine_expense = models.IntegerField(_('Machine Expense'))
    harvest_days = models.IntegerField(_('Harvest Days'))
    exp_yield = models.CharField(_('Expected Yield'), max_length=30)
    exp_harvest_date = models.DateField(_('Expected Harvest Date'))
    user = models.ForeignKey(User, related_name='user_crop', on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, related_name='farm_crop', on_delete=models.CASCADE)
    crop_image = models.FileField(upload_to='images/')


    def __str__(self):
        return self.crop_name


class CropSell(models.Model):
    crops = models.ForeignKey(Crop, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.crops.crop_name


class Seed(models.Model):
    brand = models.CharField(_('Brand'), max_length=30, blank=True)
    name = models.CharField(_('Name'), max_length=30, blank=True)
    category = models.CharField(_('Category'), max_length=30, blank=True)
    variety = models.CharField(_('Variety'), max_length=30, blank=True)
    price = models.IntegerField(_('Price'), blank=True)
    seed_image = models.FileField(upload_to='seed_images/', blank=True)


    def __str__(self):
        return self.name


class Machinery(models.Model):
    brand = models.CharField(_('Brand'), max_length=30, blank=True)
    name = models.CharField(_('Name'), max_length=30, blank=True)
    category = models.CharField(_('Category'), max_length=30, blank=True)
    price = models.IntegerField(_('Price'), blank=True)
    machine_image = models.FileField(upload_to='machine_images/', blank=True)

    def __str__(self):
        return self.name


class Others(models.Model):
    brand = models.CharField(_('Brand'), max_length=30, blank=True)
    name = models.CharField(_('Name'), max_length=30, blank=True)
    category = models.CharField(_('Category'), max_length=30, blank=True)
    price = models.IntegerField(_('Price'), blank=True)
    other_image = models.FileField(upload_to='other_images/', blank=True)

    class Meta:
        verbose_name_plural = "Others"

    def __str__(self):
        return self.name


class PesticidesAndFertilizers(models.Model):
    brand = models.CharField(_('Brand'), max_length=30, blank=True)
    name = models.CharField(_('Name'), max_length=30, blank=True)
    category = models.CharField(_('Category'), max_length=30, blank=True)
    price = models.IntegerField(_('Price'), blank=True)
    pest_image = models.FileField(upload_to='pest_images/', blank=True)

    def __str__(self):
        return self.name


class BuyRequest(models.Model):
    user = models.ForeignKey(User, related_name='seed_buy', on_delete=models.CASCADE)
    # title = models.CharField(_('Title'), max_length=30)
    seed = models.ManyToManyField(Seed, blank=True)
    machine = models.ManyToManyField(Machinery, blank=True, related_name="crop_machine")
    pest_fer = models.ManyToManyField(PesticidesAndFertilizers, blank=True)
    others = models.ManyToManyField(Others, blank=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        # print(self.seed.all())
        return str(self.user)
