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

from django.contrib.auth.models import User

from diningdeck.models import UserEaten, Restaurant

def create_user(first_name, last_name, username, password):
    if len(User.objects.filter(username=username)) != 0:
        return False

    user = User.objects.create_user(username, email="", password=password)

    user.first_name = first_name
    user.last_name = last_name
    user.save()

    return True

def save_eaten_at(restaurant_list, user):
    restaurants = Restaurant.objects.filter(name__in=restaurant_list)

    for restaurant in restaurants:
        user_eaten = UserEaten.objects.create(restaurant=restaurant, user=user)
        user_eaten.save()