from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def greet(request):
    msg='Good morning'
    return HttpResponse(msg)
def time(request):
    t=datetime.datetime.now()
    msg='The TIME is :'+str(t)
    return HttpResponse(msg)