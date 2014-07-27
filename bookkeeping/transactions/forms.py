from datetime import date

from django import forms
from django.forms.widgets import DateInput as DjangoDateInput

from bookkeeping.transactions.models import Payment, Client, Category


__author__ = 'ceasaro'


class DateInput(DjangoDateInput):
    input_type = 'date'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category


class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        year = int(kwargs.pop('year', None))
        super(PaymentForm, self).__init__(*args, **kwargs)
        if year:
            self.fields['pay_date'].initial = date(year, 1, 1)
        self.fields['tax_percentage'].initial = 21

    class Meta:
        model = Payment
        widgets = {
            'pay_date': DateInput,
        }
