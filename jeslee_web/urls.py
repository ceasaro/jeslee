from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from jeslee_web.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeslee_web.views.home', name='home'),
    # url(r'^jeslee_web/', include('jeslee_web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(template_name="home.html"), name='home'),

    # authentication
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': "auth/login.html"}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': "/"}, name='logout'),

)
