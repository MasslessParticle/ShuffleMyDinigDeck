from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages

from util import create_user

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
            context['f_name'] = first_name
            context['l_name'] = last_name
            context['username'] = username
            context['password'] = password
            context['password_verify'] = password_verify

            return render(request, 'diningdeck/register.html', context)
        else:
            messages.add_message(request, messages.SUCCESS, "Successfully registered. Please log in.")
            return redirect('diningdeck:index')

    return render(request, 'diningdeck/register.html', context)

def getsuggestion(request):
    return HttpResponse("This url returns suggestions")

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


