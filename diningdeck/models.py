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

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    cost = models.IntegerField(max_length=4)
    address = models.CharField(max_length=200)
    phone_number = models.BigIntegerField(max_length=10)
    neighborhood = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class UserEaten(models.Model):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
    did_eat = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username + " ate at " + self.restaurant.name

