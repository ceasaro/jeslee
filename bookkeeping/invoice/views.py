from django.core.exceptions import ObjectDoesNotExist

from django.core.files.base import ContentFile
from django.http import HttpResponse, Http404

from django.views.generic import  View
from lfs.order.models import Order

from bookkeeping.bookkeeping_core.models import Client
from bookkeeping.invoice.pdf import invoice_to_PDF


__author__ = 'ceasaro'


class DownloadInvoiceView(View):

    def get(self, request, *args, **kwargs):
        order_uuid = self.kwargs.get('uuid', None)
        client = Client.objects.all()[0]
        try:
            order = Order.objects.get(uuid=order_uuid)
        except ObjectDoesNotExist:
            raise Http404
        invoice_data = invoice_to_PDF(order=order, client=client)
        pdf_file = ContentFile(invoice_data)
        response = HttpResponse(pdf_file, mimetype="application/pdf")
        response['Content-Length'] = pdf_file.size
        response["Content-Disposition"] = "attachment; filename=factuur_jeslee_{0}.pdf".format(order.number)
        return response

