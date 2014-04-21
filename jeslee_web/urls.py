from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

from jeslee_web.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeslee_web.views.home', name='home'),
    # url(r'^jeslee_web/', include('jeslee_web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', HomeView.as_view(template_name="home.html"), name='home'),

    # pages
    url(r'^over-jeslee/$', TemplateView.as_view(template_name='pages/about-jeslee.html'), name='about'),
    url(r'^winkel/$', HomeView.as_view(template_name="lfs/collections.html"), name='winkel'),
    # url(r'^winkel/$', HomeView.as_view(template_name="pages/web-shop-uc.html"), name='winkel'),
    url(r'^modeshows/', include('jeslee_web.fashion_show.urls')),
#    url(r'evenementen', TemplateView.as_view(template_name='pages/evenementen.html'), name='evenementen'),
#    url(r'fotogalerij', TemplateView.as_view(template_name='pages/fotogalerij.html'), name='fotogalerij'),
    url(r'^nieuws/$', TemplateView.as_view(template_name='pages/nieuws.html'), name='nieuws'),
    url(r'^verkooppunten/$', TemplateView.as_view(template_name='pages/verkooppunten.html'), name='verkooppunten'),
    url(r'^contact/$', TemplateView.as_view(template_name='pages/contact.html'), name='contact'),

    #pages footer
    # authentication
    url(r'^bedrijfsinformatie/$', TemplateView.as_view(template_name='pages/footer/bedrijfsinformatie.html'),
        name='company-info'),
    url(r'^veilig-betalen/$', TemplateView.as_view(template_name='pages/footer/veilig-betalen.html'),
        name='save-payment'),
    url(r'^retour/$', TemplateView.as_view(template_name='pages/footer/retour.html'),
        name='return-goods'),
    url(r'^sponsoren/$', TemplateView.as_view(template_name='pages/footer/sponsoren.html'), name='sponsors'),
    # url(r'^partners/$', TemplateView.as_view(template_name='pages/footer/partners.html'), name='partners'),
    url(r'^privacy/$', TemplateView.as_view(template_name='pages/footer/privacy.html'),
        name='privacy'),
    url(r'^voorwaarden/$', TemplateView.as_view(template_name='pages/footer/voorwaarden.html'),
        name='conditions'),
    url(r'^onderhoud/$', TemplateView.as_view(template_name='pages/footer/maintenance.html'),
        name='maintenance'),

    url(r'^ideal/', include('jeslee_web.ideal.urls')),
    url(r'^ideal/ing/', include('jeslee_web.ideal.ing_tests.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': "auth/login.html"}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': "/"}, name='logout'),


)


import os
DIRNAME = os.path.dirname(__file__)

handler500 = 'lfs.core.views.server_error'

urlpatterns += patterns("",
    (r'^winkel/', include('jeslee_web.lfs_patch.core.urls')),
    (r'^manage/', include('jeslee_web.lfs_patch.manage.urls')),
)

urlpatterns += patterns("",
    (r'^reviews/', include('reviews.urls')),
    (r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    (r'^paypal/pdt/', include('paypal.standard.pdt.urls')),
)

urlpatterns += patterns("",
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, "media"), 'show_indexes': True }),
)
