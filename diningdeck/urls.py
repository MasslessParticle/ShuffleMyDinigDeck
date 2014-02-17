from django.conf.urls import patterns, url
from diningdeck import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^getsuggestion/', views.getsuggestion, name='getsuggestion'),
    url(r'^login/$', views.login, name='dologin'),
    url(r'^logout/$', views.logout, name='dologout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^restaurants/$', views.restaurant_detail, name='detail'),
    url(r'^saverestaurants/$', views.save_restaurants, name='save')
)