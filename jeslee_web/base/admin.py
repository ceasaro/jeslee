from django.contrib import admin
from jeslee_web.base.models import ClothingSize, Garment


class ClothingSizeAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClothingSize, ClothingSizeAdmin)


class GarmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Garment, GarmentAdmin)