from django.conf.urls import patterns, include, url
from django.contrib import admin

from diningdeck import urls


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DenverFood.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('diningdeck.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^diningdeck/', include('diningdeck.urls', namespace='diningdeck'))
)
