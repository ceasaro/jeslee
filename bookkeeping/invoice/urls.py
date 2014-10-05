from django.conf.urls import patterns, url

from bookkeeping.invoice.views import CreateInvoiceWizard, DownloadInvoiceView, InvoiceView, OverviewView


urlpatterns = patterns(
    'bookkeeping.invoice',
    url(r'^$', OverviewView.as_view(template_name='bookkeeping/invoice/overview.html'),
        name='invoice_home'),
    url(r'^create/$', CreateInvoiceWizard.as_view(CreateInvoiceWizard.form_list),
        name='invoice_create'),
    url(r'^(?P<uuid>[^/]+)/$', InvoiceView.as_view(),
        name='view_invoice'),
    url(r'^(?P<uuid>[^/]+)/download/$', DownloadInvoiceView.as_view(),
        name='download_invoice'),

)
