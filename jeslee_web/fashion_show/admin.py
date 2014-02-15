from django.contrib import admin
from jeslee_web.fashion_show.models import FashionRegistration


class FashionRegistrationAdmin(admin.ModelAdmin):
    pass

admin.site.register(FashionRegistration, FashionRegistrationAdmin)