from django.conf.urls import include, url
from django.http      import HttpResponse
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
import web.urls


urlpatterns = (
    # Main pages
    url(r'^works/adm/', include(web.urls)),

    url(r'^.*/', RedirectView.as_view(url='/works/adm/'), name="redirect"),
)

