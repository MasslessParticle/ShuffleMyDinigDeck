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