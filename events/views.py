from django.shortcuts import render
from .models import Events

# Create your views here.

def events(request):

    event  =  Events.objects.all