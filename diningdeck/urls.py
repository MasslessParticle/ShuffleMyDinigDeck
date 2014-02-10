from django.conf.urls import patterns, url
from diningdeck import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/register/$', views.register, name='results'),
    url(r'/getsuggestion/$', views.getsuggestion, name='vote')
)