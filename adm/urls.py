from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from adm import settings

admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Main pages
    url(r'^$', 'adm.views.index', name='index'),
    url(r'^agence/$', 'adm.views.agence', name='agence'),
    url(r'^portfolio/$', 'adm.views.portfolio', name='portfolio'),
    url(r'^equipe/$', 'adm.views.equipe', name='equipe'),
    url(r'^clients/$', 'adm.views.clients', name='clients'),
    url(r'^contact/$', 'adm.views.contact', name='contact'),

    # Admin stuff
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # DajaxIce
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

# dajaxice, needed ?
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()

#if settings.DEBUG :
urlpatterns += patterns('',
    (r'^adm.media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    (r'^adm.admin.media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT }),
)
