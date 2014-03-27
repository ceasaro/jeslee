from django.contrib import admin
from jeslee_web.fashion_show.models import FashionRegistration, FashionLocation\
    , FashionModel, FashionGarment, FashionShow


class FashionRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'size', 'fashion_show')
    list_filter = ('fashion_show', 'age', 'size')
    pass

admin.site.register(FashionRegistration, FashionRegistrationAdmin)


class FashionGarmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionGarment, FashionGarmentAdmin)


class FashionModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionModel, FashionModelAdmin)


class FashionLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionLocation, FashionLocationAdmin)


class FashionShowAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionShow, FashionShowAdmin)