from django.conf.urls import patterns, url
from jeslee_web.fashion_show.views import FashionRegistrationCreateView, FashionRegistrationDetailView\
    , FashionShowsView, FashionShowDetailView

__author__ = 'ceasaro'
urlpatterns = patterns(
    'jeslee_web.fashion_show',
    url(r'^$', FashionShowsView.as_view(template_name='fashion_show/fashion-shows.html'),
        name='fashion-shows'),
    url(r'^(?P<pk>\d+)$', FashionShowDetailView.as_view(template_name='fashion_show/fashion-show-detail.html'),
        name='fashion-show'),
    url(r'^aanmelden/$', FashionRegistrationCreateView.as_view(
        template_name='fashion_show/fashion-shows-registration.html'),
        name='fashion-registration'),
    url(r'^aanmelden/bedankt/(?P<pk>\d+)$', FashionRegistrationDetailView.as_view(
        template_name='fashion_show/fashion-shows-registration-thanks.html'),
        name='fashion-registration-thanks')
)
