from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main_site import settings

admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Main pages
    url(r'^$', 'main_site.views.index', name='index'),
    url(r'^agence/$', 'main_site.views.agence', name='agence'),
    url(r'^portfolio/$', 'main_site.views.portfolio', name='portfolio'),
    url(r'^equipe/$', 'main_site.views.equipe', name='equipe'),
    url(r'^clients/$', 'main_site.views.clients', name='clients'),
    url(r'^contact/$', 'main_site.views.contact', name='contact'),

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
