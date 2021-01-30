from django.contrib import admin

from .models import Farm, GeoTag


class FarmSearch(admin.ModelAdmin):
    search_fields = ['area', 'village', 'district', 'user_id__username', 'user_id__phone', 'user_id__name']
    list_filter = ['area', 'village', 'district', 'user_id__username', 'user_id__phone', 'user_id__name']


admin.site.register(Farm, FarmSearch)
admin.site.register(GeoTag)
