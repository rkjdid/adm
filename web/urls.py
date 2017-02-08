from django.conf.urls import include, url
from django.http      import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import views as views

admin.autodiscover()

urlpatterns = (
    # Main pages
    url(r'^$', views.index, name='index'),
    url(r'^agence/$', views.agence, name='agence'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^portfolio/(?P<pagebookId>\d+)/?$', views.portfolio, name="portfolio"),
    url(r'^equipe/$', views.equipe, name='equipe'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^contact/$', views.contact, name='contact'),

    # Admin stuff
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Zoom whole window
#    url(r'^iframe/(?P<zoom>\d+)/?$', views.index', name='index'),
)

urlpatterns += (
    url(r'^robots.txt', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
)
