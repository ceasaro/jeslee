from datetime import date

from django.core.urlresolvers import reverse
from django.db.models import Sum

from django.views.generic import CreateView, TemplateView

from bookkeeping.transactions.forms import PaymentForm, ClientForm
from bookkeeping.transactions.models import Payment


__author__ = 'ceasaro'

class FinancialYearMixin(object):

    def financial_year(self):
        return int(self.request.GET['year']) if 'year' in self.request.GET else date.today().year


class PaymentOverviewView(TemplateView, FinancialYearMixin):

    def get_context_data(self, **kwargs):
        context_data = super(PaymentOverviewView, self).get_context_data(**kwargs)
        year = self.financial_year()
        payments = Payment.objects.of_year(year)
        sum_tax = sum(payment.tax for payment in payments)
        sum_amount = payments.aggregate(Sum('amount'))
        context_data.update({
            'year': year,
            'payments': {
                'sum_amount': sum_amount['amount__sum'],
                'sum_tax': sum_tax
            },
        })
        return context_data


class ClientView(CreateView):
    form_class = ClientForm

    def get_success_url(self):
        return reverse('new_payment')


class PaymentView(CreateView, FinancialYearMixin):
    form_class = PaymentForm

    def get_form_kwargs(self):
        form_kwargs = super(PaymentView, self).get_form_kwargs()
        form_kwargs['year'] = self.financial_year()

        return form_kwargs


    def get_success_url(self):
        return reverse('bookkeeping_home')