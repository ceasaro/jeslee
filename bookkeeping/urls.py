from django.views.generic import TemplateView

__author__ = 'ceasaro'
from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    'bookkeeping',
    url(r'^$', TemplateView.as_view(template_name='bookkeeping/bookkeeping-index.html'), name='bookkeeping_home'),
    url(r'^transactions/', include('bookkeeping.transactions.urls')),
)
