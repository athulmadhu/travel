from django.shortcuts import render
from .forms import contactform
from .models import *
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request,"index.html")


def contact(req):
    if req.method == "POST":
        data = contactform(req.POST)
        if data.is_valid():
            data.save()
            messages.success(req,"Messsage is sent")
            return render(req,"contact.html")
        
    return render(req,"contact.html")

def singlepage(request):
    return render(request,"trip-single.html")

def trips1(request):
    return render(request,"trips.html")

def goa(request):
    return render(request,"Goa.html")

def kovalam(req):
    return render(req,"kovalam.html")