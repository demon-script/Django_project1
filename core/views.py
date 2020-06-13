from django.shortcuts import render, HttpResponse
from cgitb import reset

# Create your views here.

def index(request):
    return render(request,"core/index.html")

def info(request):
    return render(request,"core/info.html")

def contact(request):
    return render(request, "core/contact.html")
