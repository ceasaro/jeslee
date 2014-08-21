from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    'bookkeeping.invoice',
    url(r'^$', TemplateView.as_view(template_name='bookkeeping/invoice/overview.html'),
        name='transaction_home'),
)
