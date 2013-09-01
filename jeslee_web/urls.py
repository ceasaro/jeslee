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
    url(r'^collecties$', HomeView.as_view(template_name="lfs/collections.html"), name='collections'),

    # pages
    url(r'over-jeslee', TemplateView.as_view(template_name='pages/about-jeslee.html'), name='about'),

    # authentication
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': "auth/login.html"}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': "/"}, name='logout'),

)


import os
DIRNAME = os.path.dirname(__file__)

handler500 = 'lfs.core.views.server_error'

urlpatterns += patterns("",
    (r'^shop/', include('jeslee_web.lfs_patch.core.urls')),
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
