from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from jeslee_web.fashion_show.views import FashionRegistrationCreateView, FashionRegistrationDetailView

__author__ = 'ceasaro'
urlpatterns = patterns(
    'jeslee_web.fashion_show',
    url(r'^$', TemplateView.as_view(template_name='fashion_show/fashion_shows.html'),
        name='modeshows'),
    url(r'^aanmelden/$', FashionRegistrationCreateView.as_view(
        template_name='fashion_show/fashion_shows_registration.html'),
        name='fashion-registration'),
    url(r'^aanmelden/bedankt/(?P<pk>\d+)$', FashionRegistrationDetailView.as_view(
        template_name='fashion_show/fashion_shows_registration_thanks.html'),
        name='fashion-registration-thanks')
)
