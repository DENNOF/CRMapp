from django.http import HttpResponse
from django.shortcuts import render

def home(request, *args, **kwargs):
    return render(request, "home.html", {})
    #print(args, kwargs)
    #print(request.user)
   # return HttpResponse("<h1> Go Fuck yourself this is my first django page</h1>")
# Create your views here.
