from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View, DetailView
from django.utils.translation import ugettext as _
from lfs.core.models import Country
from lfs.core.utils import import_symbol
from lfs.order.models import Order

from jeslee_web.settings import reverse_lazy
from bookkeeping.bookkeeping_core.models import Client
from bookkeeping.invoice.forms import InvoiceForm, InvoiceItemForm
from bookkeeping.invoice.pdf import invoice_to_PDF


__author__ = 'ceasaro'


class DownloadInvoiceView(View):

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(DownloadInvoiceView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        order_uuid = self.kwargs.get('uuid', None)
        client = Client.objects.all()[0]
        try:
            order = Order.objects.get(uuid=order_uuid)
        except ObjectDoesNotExist:
            raise Http404
        invoice_data = invoice_to_PDF(order=order, client=client, filename='/tmp/testcees.pdf')
        pdf_file = ContentFile(invoice_data)
        response = HttpResponse(pdf_file, mimetype="application/pdf")
        response['Content-Length'] = pdf_file.size
        response["Content-Disposition"] = "attachment; filename=factuur_jeslee_{0}.pdf".format(order.number)
        return response


class InvoiceView(DetailView):
    model = Order
    template_name = 'bookkeeping/invoice/detail_invoice.html'

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(InvoiceView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid', None)
        try:
            # Get the single item from the filtered queryset
            obj = Order.objects.get(uuid=uuid)
        except ObjectDoesNotExist:
            raise Http404(_("No order found matching the query"))
        return obj


class CreateInvoiceWizard(SessionWizardView):
    form_1 = 'invoice'
    form_2 = 'invoice_item'
    form_list = [(form_1, InvoiceForm), (form_2, InvoiceItemForm)]
    template_list = {form_1: "bookkeeping/invoice/create_invoice.html",
                     form_2: "bookkeeping/invoice/create_invoice_item.html"}

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateInvoiceWizard, self).dispatch(*args, **kwargs)

    def get_template_names(self):
        return [self.template_list[self.steps.current]]

    def done(self, form_list, **kwargs):
        data = self.get_all_cleaned_data()
        client = data['client']
        print ('############################################################')
        print 'date = {data}'.format(data=data)
        print 'client {0}'.format(client.street)
        print ('############################################################')

        order = create_order(data, self.request)

        success_url = reverse_lazy('view_invoice',
                                   kwargs={'uuid': order.uuid})
        return HttpResponseRedirect(success_url)


def create_order(form_data, request):
    client = form_data['client']
    order = Order.objects.create(
        user=request.user,

        session=request.session.session_key,
        price=form_data['product_price_gross'],
        # tax=form_data['product_price_gross'] * form_data['product_tax'],

        customer_firstname=client.name,
        customer_lastname='',
        customer_email='',

        invoice_firstname=client.name,
        invoice_lastname='',
        invoice_company_name=client.name,
        invoice_line1='{street} {nr}'.format(street=client.street, nr=client.street_nr),
        invoice_line2='',
        invoice_city=client.city,
        invoice_state='',
        invoice_code=client.zip,
        invoice_country=Country.objects.get(code='nl'),
        invoice_phone='',


        # message=request.POST.get("message", ""),
    )
    ong = import_symbol(settings.LFS_ORDER_NUMBER_GENERATOR)
    try:
        order_numbers = ong.objects.get(id="order_number")
    except ong.DoesNotExist:
        order_numbers = ong.objects.create(id="order_number")

    try:
        order_numbers.init(request, order)
    except AttributeError:
        pass

    order.number = order_numbers.get_next()
    return order

