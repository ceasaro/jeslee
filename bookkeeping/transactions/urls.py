from django.conf.urls import patterns, url

from bookkeeping.transactions.views import PaymentCreateView, ClientCreateView, PaymentOverviewView, CategoryCreateView

__author__ = 'ceasaro'
urlpatterns = patterns(
    'bookkeeping.transactions',
    url(r'^$', PaymentOverviewView.as_view(template_name='overview.html'),
        name='bookkeeping_home'),
    url(r'^payment/new$', PaymentCreateView.as_view(template_name='payment_new.html'),
        name='new_payment'),
    url(r'^client/new$', ClientCreateView.as_view(template_name='client_new.html'),
        name='new_client'),
    url(r'^category/new$', CategoryCreateView.as_view(template_name='category_new.html'),
        name='new_category'),
)
