from django.contrib import admin

from .models import Farm, GeoTag


class FarmSearch(admin.ModelAdmin):
    search_fields = ['name', 'area', 'village', 'district', 'user_id__username', 'user_id__phone', 'user_id__name']
    list_filter = ['name', 'area', 'village', 'district', 'user_id__username', 'user_id__phone', 'user_id__name']
    list_display = ('name', 'village', 'district',)
    fieldsets = [('Farm info', {'fields': ('name', 'soil_health', 'user_id', 'geo',
                                           'area', 'village',
                                           'district', 'acres')},)]


admin.site.register(Farm, FarmSearch)
admin.site.register(GeoTag)
