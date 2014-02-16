from django.conf.urls import patterns, url
from diningdeck import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^getsuggestion/', views.getsuggestion, name='vote'),
    url(r'^login/$', views.login, name='dologin'),
    url(r'^logout/$', views.logout, name='dologout'),
    url(r'^about/$', views.logout, name='about')
)