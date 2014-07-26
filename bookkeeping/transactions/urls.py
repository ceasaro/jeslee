from django.conf.urls import patterns, url

from bookkeeping.transactions.views import PaymentView, ClientView, PaymentOverviewView


__author__ = 'ceasaro'
urlpatterns = patterns(
    '',
    url(r'^/?$', PaymentOverviewView.as_view(template_name='overview.html'),
        name='bookkeeping_home'),
    url(r'^payment/new$', PaymentView.as_view(template_name='payment_new.html'),
        name='new_payment'),
    url(r'^client/new$', ClientView.as_view(template_name='client_new.html'),
        name='new_client'),
)
