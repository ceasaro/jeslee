from bookkeeping.revenue.views import RevenueView

__author__ = 'ceasaro'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'revenue',
    url(r'^$', RevenueView.as_view(template_name='bookkeeping/revenue/year-overview.html'),
        name='revenue-year-overview'),

)
