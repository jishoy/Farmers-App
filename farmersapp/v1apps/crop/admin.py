from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _
# Register your models here.
from .models import Crop, Machinery, Seed, Others, PesticidesAndFertilizers, CropActivity, BuyRequest, CropSell


class CropSearch(admin.ModelAdmin):
    fieldsets = [('Crop info', {'fields': ('crop_name', 'exp_price', 'exp_yield', 'exp_harvest_date',
                                           'acres', 'harvest_days', 'fertilizer_expense', 'seed_expense',
                                           'machine_expense', 'total_expense', 'user', 'farm', 'crop_image')})]
    list_filter = ('user',)
    search_fields = ['crop_name']
    list_display = ('crop_name', 'user', 'farm',)


class SeedSearch(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category')
    fieldsets = [('Seed info', {'fields': ('name', 'brand', 'category')})]
    search_fields = ['name', 'brand', 'category']
    list_filter = ['name', 'brand', 'category']


class MachineSearch(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category')
    fieldsets = [('Machine info', {'fields': ('name', 'brand', 'category')})]
    search_fields = ['name', 'brand', 'category']
    list_filter = ['name', 'brand', 'category']


class PestSearch(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category')
    fieldsets = [('Pest info', {'fields': ('name', 'brand', 'category')})]
    search_fields = ['name', 'brand', 'category']
    list_filter = ['name', 'brand', 'category']


class OtherSearch(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category')
    fieldsets = [('Other info', {'fields': ('name', 'brand', 'category')})]
    search_fields = ['name', 'brand', 'category']
    list_filter = ['name', 'brand', 'category']


class BuyRequestClass(admin.ModelAdmin):
    list_display = ('user', 'approve',)
    fieldsets = [('Request info', {'fields': ('user', 'seed', 'machine', 'pest_fer', 'others', 'approve',)})]
    search_fields = ['user__name', ]
    list_filter = ['user', ]


class CropSellClass(admin.ModelAdmin):
    list_display = ('user', 'crops',)
    fieldsets = [('CropSell info', {'fields': ('user', 'crops',)})]
    search_fields = ['user__name', ]
    list_filter = ['user', ]


admin.site.register(Seed, SeedSearch)
admin.site.register(Machinery, MachineSearch)
admin.site.register(Others, OtherSearch)
admin.site.register(PesticidesAndFertilizers, PestSearch)
admin.site.register(BuyRequest, BuyRequestClass)
admin.site.register(CropSell, CropSellClass)
admin.site.register(Crop, CropSearch)
admin.site.register(CropActivity)
