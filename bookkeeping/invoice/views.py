from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.views.generic import View, DetailView
from django.utils.translation import ugettext as _
from lfs.catalog.models import Product
from lfs.core.models import Country
from lfs.core.utils import import_symbol
from lfs.order.models import Order, OrderItem

from jeslee_web.settings import reverse_lazy
from bookkeeping.bookkeeping_core.models import Client
from bookkeeping.invoice.forms import InvoiceForm, InvoiceItemForm, InvoiceCheckForm
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
    ORDER_SESSION_KEY = 'invoice_wizard_order'
    ITEMS_SESSION_KEY = 'invoice_wizard_items'
    form_step_1 = 'invoice'
    form_step_2 = 'invoice_item'
    form_step_3 = 'invoice_check'
    form_list = [(form_step_1, InvoiceForm),
                 (form_step_2, InvoiceItemForm),
                 (form_step_3, InvoiceCheckForm)]
    template_list = {form_step_1: "bookkeeping/invoice/create_invoice.html",
                     form_step_2: "bookkeeping/invoice/create_invoice_item.html",
                     form_step_3: "bookkeeping/invoice/check_invoice.html"}
    order = None

    def get_form_kwargs(self, step=None):
        if step == self.form_step_2:
            return {'request': self.request}
        return super(CreateInvoiceWizard, self).get_form_kwargs(step)

    def post(self, *args, **kwargs):
        """ extends wizard with the option to rerun a certain step.
        """
        wizard_rerun_step= self.request.POST.get('wizard_rerun_step', None)
        if wizard_rerun_step:
            # self.storage.current_step =
            form = self.get_form(data=self.request.POST, files=self.request.FILES)
            if form.is_valid():
                # if the form is valid, store the cleaned data and files.
                self.storage.set_step_data(self.steps.current, self.process_step(form))
            return self.render(form)
        return super(CreateInvoiceWizard, self).post(*args, **kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateInvoiceWizard, self).dispatch(*args, **kwargs)

    def get_template_names(self):
        return [self.template_list[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context_data = super(CreateInvoiceWizard, self).get_context_data(form, **kwargs)
        client= self.get_all_cleaned_data()['client'] if 'client' in self.get_all_cleaned_data() else None
        order = self.request.session[self.ORDER_SESSION_KEY] \
            if self.ORDER_SESSION_KEY in self.request.session else None
        items = self.request.session[self.ITEMS_SESSION_KEY] \
            if self.ITEMS_SESSION_KEY in self.request.session else []
        context_data.update({
            'order': order,
            'items': items,
            'client': client
        })
        return context_data

    def process_step(self, form):
        form_data = form.cleaned_data
        if self.steps.current == self.form_step_1:
            if self.ORDER_SESSION_KEY in self.request.session:
                # update order
                self.request.session[self.ORDER_SESSION_KEY].user = form_data['client'].user
                self.request.session[self.ORDER_SESSION_KEY].message = form_data['reference']
            else:
                # create new order
                self.request.session[self.ORDER_SESSION_KEY] = \
                    create_order(form_data, self.request)
        elif self.steps.current == self.form_step_2:
            if not self.ITEMS_SESSION_KEY in self.request.session:
                self.request.session[self.ITEMS_SESSION_KEY] = []
            # remove items if specified
            item_ids_to_remove = [int(i) for i in self.request.POST.getlist('remove_items')]  # convert list if str to id's
            stored_items = self.request.session[self.ITEMS_SESSION_KEY]  # create new list of items to keep
            items_to_keep = [i for i in stored_items if i.id not in item_ids_to_remove]  # store items to keep in session
            self.request.session[self.ITEMS_SESSION_KEY] = items_to_keep
            if not self.request.POST.get('check_invoice', None):
                item, order = \
                    add_order_item(self.request.session[self.ORDER_SESSION_KEY], form_data)

                self.request.session[self.ITEMS_SESSION_KEY].append(item)
                self.request.session[self.ORDER_SESSION_KEY] = order

        return super(CreateInvoiceWizard, self).process_step(form)

    def done(self, form_list, **kwargs):
        self.request.session[self.ORDER_SESSION_KEY].save()
        success_url = reverse_lazy('view_invoice',
                                   kwargs={'uuid': self.request.session[self.ORDER_SESSION_KEY].uuid})
        # remove order from session
        del self.request.session[self.ORDER_SESSION_KEY]
        del self.request.session[self.ITEMS_SESSION_KEY]
        return HttpResponseRedirect(success_url)


def add_order_item(order, data):
    article_price = float(data['article_price'])
    article_count = float(data['article_count'])
    item_price = article_price * article_count
    tax = data['tax']
    item_tax = item_price * tax.rate / 100
    try:
        product = Product.objects.get(name=data['name'])
    except Product.DoesNotExist:
        product = Product.objects.create(
            name=data['name'],
            slug=slugify(data['name']),
            sku=data['article_code'],
            description=data['description'],
            tax=tax,
        )
    item = OrderItem.objects.create(
        order=order,
        price_gross=item_price,
        price_net=item_price * (100 - tax.rate) / 100,
        tax=item_tax,
        product=product,
        product_sku=data['article_code'],
        product_amount=article_count,
        product_name=data['name'],
        product_price_net=article_price * (100-tax.rate) / 100,
        product_price_gross=article_price,
        product_tax=article_price * tax.rate / 100,
    )
    order.price += item_price
    order.tax += item_tax
    return item, order


def create_order(form_data, request):
    client = form_data['client']
    order = Order.objects.create(
        user=client.user,
        message=form_data['reference'],

        session=request.session.session_key,
        # tax=form_data['product_price_gross'] * form_data['product_tax'],

        customer_firstname=client.name,
        customer_lastname='',
        customer_email=client.user.email,

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

