import StringIO
from abc import ABCMeta
import csv

from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView, View

from bookkeeping.bookkeeping_core.models import Category, Client
from bookkeeping.bookkeeping_core.mixins import FinancialYearMixin
from bookkeeping.transactions.forms import PaymentForm, CategoryForm
from bookkeeping.transactions.models import Payment
from bookkeeping.transactions.utils import get_payment_quarter_data


__author__ = 'ceasaro'


class AbstractPaymentView(FinancialYearMixin):
    __metaclass__ = ABCMeta
    default_order_by = 'pay_date'

    def get_order_by(self):
        return self.request.GET.get('ob', self.default_order_by)

    def filter_on_category(self, payments):
        category = self.request.GET.get('category', None)
        if category:
            try:
                self.selected_category = Category.objects.get(id=int(category))
                payments = payments.filter(category=self.selected_category)
            except ValueError:
                pass
            except Category.DoesNotExist:
                pass
        return payments

    def filter_on_client(self, payments):
        client = self.request.GET.get('client', None)
        if client:
            try:
                self.selected_client = Client.objects.get(id=int(client))
                payments = payments.filter(client=self.selected_client)
            except ValueError:
                pass
            except Client.DoesNotExist:
                pass
        return payments

    def get_payments(self):
        year = self.financial_year()
        order_by = self.get_order_by()
        payments = Payment.objects.of_year(year).order_by(order_by)

        # filter on category
        payments = self.filter_on_category(payments)
        # filter on client
        payments = self.filter_on_client(payments)

        return payments


class PaymentOverviewView(TemplateView, AbstractPaymentView):

    payments_on_page = 20
    selected_category = None
    selected_client = None

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(PaymentOverviewView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(PaymentOverviewView, self).get_context_data(**kwargs)
        payment_list = self.get_payments()
        payment_paginator = Paginator(payment_list, self.payments_on_page)
        page = self.request.GET.get('page')
        try:
            payments = payment_paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            payments = payment_paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            payments = payment_paginator.page(payment_paginator.num_pages)
        # sum_tax = sum(payment.tax for payment in payment_list)
        # sum_amount = payment_list.aggregate(Sum('amount'))
        payment_quarter_data = get_payment_quarter_data(payment_list)

        payment_data = {
            'list': payments,
            'ordered_by': self.get_order_by(),
        }
        payment_data.update(payment_quarter_data)

            # k1_amount =
        context_data.update({
            'payments': payment_data,
            'categories': Category.objects.viewable(),
            'selected_category': self.selected_category,
            'clients': Client.objects.viewable(),
            'selected_client': self.selected_client,
        })
        return context_data


class PaymentCreateView(CreateView, FinancialYearMixin):
    form_class = PaymentForm

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(PaymentCreateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        form_kwargs = super(PaymentCreateView, self).get_form_kwargs()
        form_kwargs['year'] = self.financial_year()
        return form_kwargs

    def get_success_url(self):
        return reverse('transaction_home')


class PaymentUpdateView(UpdateView, FinancialYearMixin):
    model = Payment
    form_class = PaymentForm

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(PaymentUpdateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        form_kwargs = super(PaymentUpdateView, self).get_form_kwargs()
        form_kwargs['year'] = self.financial_year()
        return form_kwargs

    def get_success_url(self):
        return reverse('transaction_home')


class CategoryCreateView(CreateView):
    form_class = CategoryForm

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('new_payment')


class DownloadPaymentsView(View, AbstractPaymentView):

    header_row = ["datum", "klant", "categorie", "bedrag", "belasting", "omschrijving"]
    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(DownloadPaymentsView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        tmp_csv_file = StringIO.StringIO()
        tmp_csv_file.write(u'\ufeff'.encode('utf8'))
        csv_writer = csv.writer(tmp_csv_file, delimiter=',', quotechar='"')
        csv_writer.writerow(self.header_row)

        def data():
            payments = self.get_payments()
            for payment in payments:
                row = [payment.pay_date,            # datum
                       payment.client,              # klant
                       payment.category,            # categorie
                       payment.amount,              # bedrag
                       payment.tax,                 # belasting
                       payment.description]         # omschrijving
                csv_writer.writerow(row)
            yield tmp_csv_file.getvalue()

        response = HttpResponse(data(), mimetype="text/csv")
        response["Content-Disposition"] = "attachment; filename=transactions.csv"
        return response


