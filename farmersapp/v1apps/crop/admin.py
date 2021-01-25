from django.contrib import admin

# Register your models here.
from .models import Crop, Machinery, Seed, Others, PesticidesAndFertilizers, CropActivity, BuyRequest, CropSell

# admin.site.register(Crop)
admin.site.register(Seed)
admin.site.register(Machinery)
admin.site.register(Others)
admin.site.register(PesticidesAndFertilizers)
admin.site.register(BuyRequest)
admin.site.register(CropSell)
admin.site.register(Crop)
admin.site.register(CropActivity)


# class PostImageAdmin(admin.StackedInline):
#     model = CropImage
#
#
# @admin.register(Crop)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]
#
#     class Meta:
#         model = Crop
#
#
# @admin.register(CropImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass