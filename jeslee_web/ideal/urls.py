from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from jeslee_web.fashion_show.views import FashionRegistrationCreateView, FashionRegistrationDetailView\
    , FashionShowsView, FashionShowDetailView
from jeslee_web.ideal.views import IdealOrder

__author__ = 'ceasaro'
urlpatterns = patterns(
    'jeslee_web.ideal',
    url(r'^order/(?P<pk>\d+)$', IdealOrder.as_view(
        template_name='ideal/ideal-form.html'),
        name='ideal-form'),
    url(r'^success/$', TemplateView.as_view(template_name='ideal/ideal-success.html'),
        name='ideal-success'),
    url(r'^cancel/$', TemplateView.as_view(template_name='ideal/ideal-cancel.html'),
        name='ideal-cancel'),
    url(r'^error/$', TemplateView.as_view(template_name='ideal/ideal-error.html'),
        name='ideal-error'),
    url(r'^failure/$', TemplateView.as_view(template_name='ideal/ideal-failure.html'),
        name='ideal-failure'),
)
