from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View, DetailView, TemplateView
from django.utils.translation import ugettext as _
from lfs.order.models import Order

from bookkeeping.bookkeeping_core.mixins import FinancialYearMixin
from bookkeeping.invoice.utils import add_order_item, create_order, get_invoice_quarter_data
from jeslee_web.settings import reverse_lazy
from bookkeeping.bookkeeping_core.models import Client
from bookkeeping.invoice.forms import InvoiceForm, InvoiceItemForm, InvoiceCheckForm
from bookkeeping.invoice.pdf import invoice_to_PDF


__author__ = 'ceasaro'


class OverviewView(FinancialYearMixin, TemplateView):
    template_name = 'bookkeeping/invoice/overview.html'

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(OverviewView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(OverviewView, self).get_context_data(**kwargs)
        year = self.financial_year()
        orders = Order.objects.filter(created__year=str(year))
        orders_data = get_invoice_quarter_data(orders)
        orders_data['count'] = len(orders)
        context_data['orders'] = orders_data
        return context_data


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
        # invoice_data = invoice_to_PDF(order=order, client=client, filename='/tmp/testcees.pdf')
        invoice_data = invoice_to_PDF(order=order, client=client)
        pdf_file = ContentFile(invoice_data)
        response = HttpResponse(pdf_file, mimetype="application/pdf")
        response['Content-Length'] = pdf_file.size
        response["Content-Disposition"] = "attachment; filename=factuur_jeslee_{0}.pdf".format(order.number)
        return response


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
                self.request.session[self.ORDER_SESSION_KEY].invoice_line2 = form_data['reference']
                self.request.session[self.ORDER_SESSION_KEY].message = form_data['message']
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
            items_to_keep = [(i,j) for i,j in stored_items if i not in item_ids_to_remove]  # store items to keep in session
            self.request.session[self.ITEMS_SESSION_KEY] = items_to_keep
            if not self.request.POST.get('check_invoice', None):
                # only store form data if user doesn't want to check the invoice
                item_id = len(self.request.session[self.ITEMS_SESSION_KEY]) + 1
                form_data['price_gross'] = float(form_data['article_price']) * float(form_data['article_count'])
                self.request.session[self.ITEMS_SESSION_KEY].append((item_id, form_data))

        return super(CreateInvoiceWizard, self).process_step(form)

    def done(self, form_list, **kwargs):
        order = self.request.session[self.ORDER_SESSION_KEY]
        for i, item_form_data in self.request.session[self.ITEMS_SESSION_KEY]:
            add_order_item(order, item_form_data)
        order.save()
        success_url = reverse_lazy('view_invoice',
                                   kwargs={'uuid': self.request.session[self.ORDER_SESSION_KEY].uuid})
        # remove order from session
        del self.request.session[self.ORDER_SESSION_KEY]
        del self.request.session[self.ITEMS_SESSION_KEY]
        return HttpResponseRedirect(success_url)
