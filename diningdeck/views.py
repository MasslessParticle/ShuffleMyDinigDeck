from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'message': 'Hello World!'}
    return render(request, 'diningdeck/index.html', context)

def register(request):
    return HttpResponse("This is the registration page")

def getsuggestion(request):
    return HttpResponse("This url returns suggestions")