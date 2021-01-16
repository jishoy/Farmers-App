from django.contrib import admin

# Register your models here.
from .models import Farm, GeoTag

admin.site.register(Farm)
admin.site.register(GeoTag)