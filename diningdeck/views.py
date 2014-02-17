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

from random import shuffle

from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages
from django.db.models import Q
from django.forms import model_to_dict
from django.utils.html import strip_tags

from diningdeck.models import Restaurant, UserEaten
from diningdeck.util import create_user, save_eaten_at

import json
import HTMLParser

# Create your views here.
def index(request):
    context = {'name': None}
    user = request.user

    if user.is_authenticated():
        if user.first_name != "":
           name = user.first_name
        else:
            name = user.username

        context['name'] = name

    return render(request, 'diningdeck/index.html', context)

def register(request):
    context = {}
    context.update(csrf(request))

    if request.POST:

        first_name = ""
        last_name = ""

        if 'f_name' in request.POST:
            first_name = request.POST['f_name']

        if 'l_name' in request.POST:
            last_name = request.POST['l_name']

        username = request.POST['username']
        password = request.POST['password']
        password_verify = request.POST['password_verify']

        error = False

        if username == "" or password == "":
            messages.add_message(request, messages.ERROR, "Username and password can't be blank")
            error = True

        if password != password_verify:
            messages.add_message(request, messages.ERROR, "Passwords don't match.")
            error = True

        if not create_user(first_name, last_name, username, password):
            messages.add_message(request, messages.ERROR, "Username is already used, please select another.")
            error = True

        if error:
            context['f_name'] = strip_tags(first_name)
            context['l_name'] = strip_tags(last_name)
            context['username'] = strip_tags(username)
            context['password'] = strip_tags(password)
            context['password_verify'] = strip_tags(password_verify)

            return render(request, 'diningdeck/register.html', context)
        else:
            messages.add_message(request, messages.SUCCESS, "Successfully registered. Please log in.")
            return redirect('diningdeck:index')

    return render(request, 'diningdeck/register.html', context)

def getsuggestion(request):
    context = {}
    context.update(csrf(request))

    if request.POST:
        price = request.POST['price-select']
        neighborhood = request.POST['hood-select']
        restaurants = Restaurant.objects.all()

        if request.user.is_authenticated():
            html_parser = HTMLParser.HTMLParser()

            if 'eaten-at' in request.POST:
                eaten_at = [html_parser.unescape(entry) for entry in request.POST.getlist('eaten-at')]
                save_eaten_at(eaten_at, request.user)

            user = request.user
            ate_at = UserEaten.objects.filter(user=user)
            ate_at_list = [entry.restaurant.pk for entry in ate_at]
            restaurants = restaurants.filter(~Q(pk__in=ate_at_list))

        if price != "":
            restaurants = restaurants.filter(cost__lte=price)

        if neighborhood != "":
            restaurants = restaurants.filter(neighborhood__icontains=neighborhood)

        restaurant_list = list(restaurants)
        shuffle(restaurant_list)
        restaurant_list = restaurant_list[:3]

        response = {}
        response['authenticated'] = request.user.is_authenticated()
        response['restaurants'] = []

        for restaurant in restaurant_list:
            restaurant.cost = int(restaurant.cost) * "$"
            phone_number = str(restaurant.phone_number)
            restaurant.phone_number = phone_number[:3] + "-" + phone_number[3:6] + "-" + phone_number[6:]
            response['restaurants'].append(model_to_dict(restaurant))

        json_response = json.dumps(response)

        return HttpResponse(json_response, content_type='application/json')
    else:
        return redirect(request.path)

def login(request):
    if request.POST:
        error = False

        if 'username' in request.POST:
            username = request.POST['username']
        else:
            error = True

        if 'password' in request.POST:
            password = request.POST['password']
        else:
            error = True

        if not error:
            user = auth.authenticate(username=username, password=password)

            context = {'name': None}
            context.update(csrf(request))

            if user is not None:
                auth.login(request, user)

    return redirect('diningdeck:index')

def logout(request):
    auth.logout(request)
    return redirect('diningdeck:index')

def restaurant_detail(request):
    user = request.user

    if user.is_authenticated():
        name = user.username
        if user.first_name != "":
            name = user.first_name

        context = {'name' : name}
        restaurants = Restaurant.objects.all()
        context['restaurants'] = restaurants

        user_eaten = UserEaten.objects.filter(user=user)

        user_ate_at = {}
        for eaten in user_eaten:
            user_ate_at[eaten.restaurant.name] = True

        context['user_ate_at'] = user_ate_at
        return render(request, 'diningdeck/detail.html', context)
    else:
        return redirect('diningdeck:index')

def save_restaurants(request):
    context = {}
    context.update(csrf(request))

    user = request.user

    if request.POST and user.is_authenticated():
        html_parser = HTMLParser.HTMLParser()
        eaten = [html_parser.unescape(entry) for entry in request.POST.getlist('eaten')]
        not_eaten = [html_parser.unescape(entry) for entry in request.POST.getlist('not-eaten')]
        user_eaten = UserEaten.objects.filter(user=user)

        for eaten_record in user_eaten:
            restaurant_name = eaten_record.restaurant.name
            if restaurant_name in not_eaten:
                eaten_record.delete()

        for eaten_restaurant in eaten:
            restaurant = Restaurant.objects.get(name=eaten_restaurant)
            new_eaten = UserEaten.objects.create(user=user, restaurant=restaurant)
            new_eaten.save()

        response = {'success' : True}

        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return redirect('diningdeck:index')

def about(request):
    return render(request, 'diningdeck/about.html')


