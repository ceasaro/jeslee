from datetime import date

from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.views.generic import CreateView, TemplateView

from bookkeeping.transactions.forms import PaymentForm, ClientForm, CategoryForm
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

    def get_order_by(self):
        return self.request.GET.get('ob', self.default_order_by)

    def get_payments(self):
        year = self.financial_year()
        order_by = self.get_order_by()
        return Payment.objects.of_year(year).order_by(order_by)

    def get_context_data(self, **kwargs):
        context_data = super(PaymentOverviewView, self).get_context_data(**kwargs)
        payments = self.get_payments()
        sum_tax = sum(payment.tax for payment in payments)
        sum_amount = payments.aggregate(Sum('amount'))
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

    def get_form_kwargs(self):
        form_kwargs = super(PaymentCreateView, self).get_form_kwargs()
        form_kwargs['year'] = self.financial_year()

        return form_kwargs


    def get_success_url(self):
        return reverse('bookkeeping_home')


class ClientCreateView(CreateView):
    form_class = ClientForm

    def get_success_url(self):
        return reverse('new_payment')


class CategoryCreateView(CreateView):
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('new_payment')
