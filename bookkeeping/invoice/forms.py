from django import forms
from lfs.order.models import OrderItem

from bookkeeping.bookkeeping_core.models import Client


__author__ = 'ceasaro'


class InvoiceForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=True)
    reference = forms.CharField(max_length=128)


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product_name', 'product_amount', 'product_price_gross', 'price_gross', ]
