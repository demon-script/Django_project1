from django.shortcuts import render, HttpResponse
from cgitb import reset

# Create your views here.

commonhtml ='''
             <title>Demonscript!!:.. </title>
             <center>
                  <h1> Mi Sitio Personal</h1>
             </center>
             <ul>
                  <li><a href='/'>Home</a></li>
                  <li><a href='/info'>Info del sitio</a></li>
                  <li></li>
                  <li></li>
             </ul>
             '''

def index(request):
    return render(request,"core/index.html")

def info(request):
    return render(request,"core/info.html")
def services(request):
    return render(request, "core/services.html")
def contact(request):
    return render(request, "core/contact.html")
