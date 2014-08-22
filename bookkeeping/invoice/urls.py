from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from bookkeeping.invoice.views import InvoiceCreateView


urlpatterns = patterns(
    'bookkeeping.invoice',
    url(r'^$', TemplateView.as_view(template_name='bookkeeping/invoice/overview.html'),
        name='invoice_home'),
    url(r'^create/$', InvoiceCreateView.as_view(template_name='bookkeeping/invoice/overview.html'),
        name='invoice_create'),

)
