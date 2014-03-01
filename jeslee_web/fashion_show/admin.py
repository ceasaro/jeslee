from django.contrib import admin
from jeslee_web.fashion_show.models import FashionRegistration, FashionLocation, FashionModel, FashionGarment, FashionShow


class FashionRegistrationAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionRegistration, FashionRegistrationAdmin)


class FashionLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionLocation, FashionLocationAdmin)


class FashionModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionModel, FashionModelAdmin)


class FashionGarmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionGarment, FashionGarmentAdmin)


class FashionShowAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionShow, FashionShowAdmin)
