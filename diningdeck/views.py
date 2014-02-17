from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.db.models import Q
from django.forms import model_to_dict
from django.utils.html import strip_tags

from diningdeck.models import Restaurant, UserEaten
from diningdeck.util import create_user

from random import shuffle
import json

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
            user_pk = request.user.pk
            ate_at = UserEaten.objects.filter(user=user_pk)

            for restaurant in ate_at:
                restaurants.filter(~Q(id=restaurant.restaurant.pk))

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


