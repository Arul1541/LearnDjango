from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
    return HttpResponse('<h1>First</h1>')
def two(request):
    return HttpResponse('<h2>second</h2>')
def register(request):
    return render(request,"secondapp/a.html")