from django.shortcuts import render
from services.models import New_Project

# Create your views here.
def services(request):
    projects = New_Project.objects.all()
    return render(request, "services/services.html",{'projects':projects})