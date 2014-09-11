from django import forms
from lfs.tax.models import Tax

from bookkeeping.bookkeeping_core.models import Client


__author__ = 'ceasaro'


class InvoiceForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=True)
    reference = forms.CharField(max_length=128)


class InvoiceItemForm(forms.Form):

    article_code = forms.CharField(max_length=32)
    name = forms.CharField(max_length=80)
    description = forms.CharField(widget=forms.Textarea, required=False)
    article_count = forms.IntegerField(initial=1)
    article_price = forms.DecimalField(decimal_places=2)
    tax = forms.ModelChoiceField(queryset=Tax.objects.all())
    remove_items = forms.CharField(widget=forms.MultipleHiddenInput, required=False)

    class Meta:
        fields = ['remove_items', 'article_code', 'name', 'description',
                  'article_count', 'article_price', 'tax']

    def clean(self):
        if self.request.POST.get('check_invoice', None):
            # clear all validation errors cause we're check the invoice in the next step.
            self._errors = None
        return super(InvoiceItemForm, self).clean()


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(InvoiceItemForm, self).__init__(*args, **kwargs)
        self.fields['tax'].initial = Tax.objects.all()[0]


class InvoiceCheckForm(forms.Form):
    pass
