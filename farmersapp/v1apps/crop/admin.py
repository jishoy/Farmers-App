from django.contrib import admin

# Register your models here.
from .models import Crop, Machinery, Seed, Others, PesticidesAndFertilizers, BuyRequest

admin.site.register(Crop)
admin.site.register(Seed)
admin.site.register(Machinery)
admin.site.register(Others)
admin.site.register(PesticidesAndFertilizers)
admin.site.register(BuyRequest)
