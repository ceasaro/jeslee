from datetime import date

from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView

from bookkeeping.transactions.forms import PaymentForm, CategoryForm
from bookkeeping.transactions.models import Payment


__author__ = 'ceasaro'


class FinancialYearMixin(object):

    def financial_year(self):
        """
        The financial year bound to the request as 'request.financial_year'
        return: the financial year form to request GET params if not found the current year is returned.
        """
        this_year = date.today().year
        financial_year = int(self.request.GET.get('year', this_year))
        self.request.financial_year = financial_year
        self.request.financial_years = range(this_year-5, this_year+1)
        return financial_year


class PaymentOverviewView(TemplateView, FinancialYearMixin):

    default_order_by = 'pay_date'
    payments_on_page = 20

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(PaymentOverviewView, self).dispatch(*args, **kwargs)

    def get_order_by(self):
        return self.request.GET.get('ob', self.default_order_by)

    def get_payments(self):
        year = self.financial_year()
        order_by = self.get_order_by()
        return Payment.objects.of_year(year).order_by(order_by)

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
        sum_tax = sum(payment.tax for payment in payment_list)
        sum_amount = payment_list.aggregate(Sum('amount'))
        context_data.update({
            'payments': {
                'list': payments,
                'sum_amount': sum_amount['amount__sum'],
                'sum_tax': sum_tax,
                'ordered_by': self.get_order_by()
            },
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
