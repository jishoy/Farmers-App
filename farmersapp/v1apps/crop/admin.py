from django.contrib import admin

# Register your models here.
from .models import Crop, Machinery, Seed, Others, PesticidesAndFertilizers, CropActivity, BuyRequest, CropSell


class CropSearch(admin.ModelAdmin):
    search_fields = ['crop_name']


class SeedSearch(admin.ModelAdmin):
    search_fields = ['name', 'brand', 'category']


class MachineSearch(admin.ModelAdmin):
    search_fields = ['name', 'brand', 'category']


class PestSearch(admin.ModelAdmin):
    search_fields = ['name', 'brand', 'category']


class OtherSearch(admin.ModelAdmin):
    search_fields = ['name', 'brand', 'category']


admin.site.register(Seed, SeedSearch)
admin.site.register(Machinery, MachineSearch)
admin.site.register(Others, OtherSearch)
admin.site.register(PesticidesAndFertilizers, PestSearch)
admin.site.register(BuyRequest)
admin.site.register(CropSell)
admin.site.register(Crop, CropSearch)
admin.site.register(CropActivity)

