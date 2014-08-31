from bookkeeping.client.views import ClientView, ClientCreateView, ClientUpdateView

__author__ = 'ceasaro'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'bookkeeping',
    url(r'^$', ClientView.as_view(template_name='bookkeeping/client/client-overview.html'),
        name='client_home'),
    url(r'^new$', ClientCreateView.as_view(template_name='bookkeeping/client/client-create.html'),
        name='client_create'),
    url(r'^(?P<pk>[\w-]+)/update$', ClientUpdateView.as_view(template_name='bookkeeping/client/client-update.html'),
        name='client_update'),

)
