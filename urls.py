from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Main pages
    url(r'^$', 'ateliers_a.main_site.views.index', name='index'),
    url(r'^agence/$', 'ateliers_a.main_site.views.agence', name='agence'),
    url(r'^portfolio/$', 'ateliers_a.main_site.views.portfolio', {'tab':''}, name='portfolio'),
    url(r'^portfolio/design/$', 'ateliers_a.main_site.views.portfolio', {'tab':'design'}, name='portfolio'),
    url(r'^portfolio/photo/$', 'ateliers_a.main_site.views.portfolio', {'tab':'photo'}, name='portfolio'),
    url(r'^portfolio/web/$', 'ateliers_a.main_site.views.portfolio', {'tab':'web'}, name='portfolio'),
    url(r'^portfolio/com/$', 'ateliers_a.main_site.views.portfolio', {'tab':'com'}, name='portfolio'),
    url(r'^portfolio/marketo/$', 'ateliers_a.main_site.views.portfolio', {'tab':'marketo'}, name='portfolio'),
    url(r'^portfolio/marketd/$', 'ateliers_a.main_site.views.portfolio', {'tab':'marketd'}, name='portfolio'),
    url(r'^equipe/$', 'ateliers_a.main_site.views.equipe', name='equipe'),
    url(r'^clients/$', 'ateliers_a.main_site.views.clients', name='clients'),
    url(r'^contact/$', 'ateliers_a.main_site.views.contact', name='contact'),
    # url(r'^ateliers_a/', include('ateliers_a.foo.urls')),

    # Admin stuff
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # DajaxIce
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

# dajaxice, needed ?
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()

from ateliers_a import settings

#if settings.DEBUG :
urlpatterns += patterns('',
    (r'^adm.media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    (r'^adm.admin.media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT }),
)
