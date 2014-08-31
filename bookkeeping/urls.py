from bookkeeping.views import FinancialHomeView

__author__ = 'ceasaro'
from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    'bookkeeping',
    url(r'^$', FinancialHomeView.as_view(template_name='bookkeeping/bookkeeping-index.html'), name='bookkeeping_home'),
    url(r'^transactions/', include('bookkeeping.transactions.urls')),
    url(r'^invoice/', include('bookkeeping.invoice.urls')),
    url(r'^client/', include('bookkeeping.client.urls')),
)
