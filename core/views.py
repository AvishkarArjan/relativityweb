from django.shortcuts import render
from .models import Return

def home(request):
    returns = Return.objects.all().order_by('-date')  # latest first
    return render(request, 'home.html', {'returns': returns})

def about(request):
    return render(request, 'about.html')

