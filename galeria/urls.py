from django.conf.urls import patterns, include, url
from cuadros.admin import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'galeria.views.home', name='home'),
    # url(r'^galeria/', include('galeria.foo.urls')),
      url(r'^$', 'cuadros.views.inicio'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
