from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from jeslee_web.fashion_show.views import FashionRegistrationCreateView, FashionRegistrationDetailView\
    , FashionShowsView, FashionShowDetailView
from jeslee_web.ideal.ing_tests.views import IngTest1View, IngTest2View, IngTest3View, IngTest4View, IngTest5View, \
    IngTest6View, IngTest7View
from jeslee_web.ideal.views import IdealOrderView

__author__ = 'ceasaro'
urlpatterns = patterns(
    'jeslee_web.ideal.ing_tests',
    url(r'^test_1/$', IngTest1View.as_view(template_name='ideal/ing-test/ing-test.html'),
        name='ing_ideal_test_1'),
    url(r'^test_2/$', IngTest2View.as_view(template_name='ideal/ing-test/ing-test.html'),
        name='ing_ideal_test_1'),
    url(r'^test_3/$', IngTest3View.as_view(template_name='ideal/ing-test/ing-test.html'),
        name='ing_ideal_test_1'),
    url(r'^test_4/$', IngTest4View.as_view(template_name='ideal/ing-test/ing-test.html'),
        name='ing_ideal_test_1'),
    url(r'^test_5/$', IngTest5View.as_view(template_name='ideal/ing-test/ing-test.html'),
        name='ing_ideal_test_1'),
    url(r'^test_6/$', IngTest6View.as_view(template_name='ideal/ing-test/ing-test.html'),
        name='ing_ideal_test_1'),
    url(r'^test_7/$', IngTest7View.as_view(template_name='ideal/ing-test/ing-test.html'),
        name='ing_ideal_test_1'),
)
