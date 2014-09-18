from datetime import date

from django import forms
from django.forms.widgets import DateInput as DjangoDateInput

from bookkeeping.transactions.models import Payment, Category


__author__ = 'ceasaro'


class DateInput(DjangoDateInput):
    input_type = 'date'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category


class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        year = int(kwargs.pop('year', None))
        super(PaymentForm, self).__init__(*args, **kwargs)
        if year:
            self.fields['pay_date'].initial = date(year, 1, 1)

    class Meta:
        model = Payment
        widgets = {
            'pay_date': DateInput,
        }
        fields = ['pay_date', 'amount', 'description', 'client', 'category', 'tax']
