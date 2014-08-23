from django.views.generic import TemplateView
from lfs.order.models import Order

from bookkeeping.bookkeeping_core.models import Client
from bookkeeping.invoice.pdf import invoice_to_PDF


__author__ = 'ceasaro'


class InvoiceCreateView(TemplateView):

    def get(self, request, *args, **kwargs):
        client = Client.objects.all()[0]
        order = Order.objects.get(id=1)
        invoice_to_PDF(client=client, order=order)
        return super(InvoiceCreateView, self).get(request, *args, **kwargs)

