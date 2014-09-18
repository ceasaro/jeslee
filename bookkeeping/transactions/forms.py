from datetime import date

from django import forms
from django.conf import settings
from django.forms.widgets import DateInput as DjangoDateInput

from bookkeeping.transactions.models import Payment, Category


__author__ = 'ceasaro'


class DateInput(DjangoDateInput):
    input_type = 'date'

    def __init__(self, attrs=None, format=settings.DATE_INPUT_FORMATS[0]):
        super(DateInput, self).__init__(attrs, format)


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
