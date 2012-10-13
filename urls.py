from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Main pages
    url(r'^$', 'ateliers_a.main_site.views.index', name='index'),
    url(r'^agence/$', 'ateliers_a.main_site.views.agence', name='agence'),
    url(r'^portfolio/$', 'ateliers_a.main_site.views.portfolio', name='portfolio'),
    url(r'^equipe/$', 'ateliers_a.main_site.views.equipe', name='equipe'),
    url(r'^clients/$', 'ateliers_a.main_site.views.clients', name='clients'),
    url(r'^contact/$', 'ateliers_a.main_site.views.contact', name='contact'),
    # url(r'^ateliers_a/', include('ateliers_a.foo.urls')),

    # Admin stuff
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

from ateliers_a import settings

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^adm.media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    )
