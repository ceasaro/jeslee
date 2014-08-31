from django import forms
from lfs.order.models import OrderItem

from bookkeeping.bookkeeping_core.models import Client


__author__ = 'ceasaro'


class InvoiceForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=True)
    reference = forms.CharField(max_length=128)


class InvoiceItemForm(forms.Form):

    article_code = forms.CharField(max_length=32)
    name = forms.CharField(max_length=80)
    article_count = forms.IntegerField(initial=1)
    article_price = forms.DecimalField(decimal_places=2)
    tax = forms.ChoiceField(choices=((0.21,'21 %'), (0.06, '6%')))

    class Meta:
        model = OrderItem
        fields = ['article_code', 'name', 'article_count', 'article_price', 'tax']
