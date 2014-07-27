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
        financial_year = int(self.request.GET['year']) if 'year' in self.request.GET else this_year
        self.request.financial_year = financial_year
        self.request.financial_years = range(this_year-5, this_year+1)
        return financial_year


class PaymentOverviewView(TemplateView, FinancialYearMixin):

    def get_context_data(self, **kwargs):
        context_data = super(PaymentOverviewView, self).get_context_data(**kwargs)
        year = self.financial_year()
        payments = Payment.objects.of_year(year)
        sum_tax = sum(payment.tax for payment in payments)
        sum_amount = payments.aggregate(Sum('amount'))
        context_data.update({
            'payments': {
                'sum_amount': sum_amount['amount__sum'],
                'sum_tax': sum_tax
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
