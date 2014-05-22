from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from jeslee_web.ideal.views import IdealOrderView, IdealSuccessView, IdealCancelView, IdealErrorView

__author__ = 'ceasaro'
urlpatterns = patterns(
    'jeslee_web.ideal',
    url(r'^order/(?P<pk>\d+)$', IdealOrderView.as_view(
        template_name='ideal/ideal-form.html'),
        name='ideal-form'),
    url(r'^success/(?P<pk>\d+)$', IdealSuccessView.as_view(template_name='ideal/ideal-success.html'),
        name='ideal-success'),
    url(r'^cancel/(?P<pk>\d+)$', IdealCancelView.as_view(template_name='ideal/ideal-cancel.html'),
        name='ideal-cancel'),
    url(r'^error/(?P<pk>\d+)$', IdealErrorView.as_view(template_name='ideal/ideal-error.html'),
        name='ideal-error'),
    url(r'^failure/(?P<pk>\d+)$', IdealErrorView.as_view(template_name='ideal/ideal-failure.html'),
        name='ideal-failure'),
)
