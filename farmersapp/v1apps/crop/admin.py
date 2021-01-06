from django.contrib import admin

# Register your models here.
from .models import Crop, Machinery, Seed

admin.site.register(Crop)
admin.site.register(Seed)
admin.site.register(Machinery)
