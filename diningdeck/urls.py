'''
This file is part of Shuffle My Dining Deck.

Shuffle My Dining Deck is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Shuffle My Dining Deck is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

Author: Travis Patterson (masslessparticle@gmail.com)
'''

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