from django.conf.urls import patterns, url

from bookkeeping.transactions.views import PaymentCreateView, PaymentOverviewView, CategoryCreateView, PaymentUpdateView, \
    DownloadPaymentsView

__author__ = 'ceasaro'
urlpatterns = patterns(
    'bookkeeping.transactions',
    url(r'^$', PaymentOverviewView.as_view(template_name='bookkeeping/transactions/overview.html'),
        name='transaction_home'),
    url(r'^payment/new$', PaymentCreateView.as_view(template_name='bookkeeping/transactions/payment_new.html'),
        name='new_payment'),
    url(r'^payment/(?P<pk>[\w-]+)/edit$', PaymentUpdateView.as_view(template_name='bookkeeping/transactions/payment_update.html'),
        name='update_payment'),
    url(r'^category/new$', CategoryCreateView.as_view(template_name='bookkeeping/transactions/category_new.html'),
        name='new_category'),
    url(r'^download$', DownloadPaymentsView.as_view(),
        name='download_transactions'),

)
