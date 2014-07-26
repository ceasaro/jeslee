from django.contrib import admin

from bookkeeping.transactions.models import Payment, Client


class PaymentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Payment, PaymentAdmin)


class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)