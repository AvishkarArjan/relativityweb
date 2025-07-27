from django.shortcuts import render
from .models import Return

def home(request):
    returns = Return.objects.all().order_by('-date')  # latest first
    # returns = []
    """
    Date	Strategy	Return (%)	Notes
    July 27, 2025	Nebula-Mark1	12.00	The return %age should be dynamically rendered on the page.
    """
    return render(request, 'home.html', {'returns': returns})

def about(request):
    return render(request, 'about.html')

def nebula(request):
    return render(request, 'nebula.html')
