from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    cost = models.IntegerField(max_length=4)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=10)
    neighborhood = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class UserEaten(models.Model):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
    did_eat = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username + " ate at " + self.restaurant.name + ": " + str(self.did_eat)

