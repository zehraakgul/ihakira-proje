from django.shortcuts import render
from .models import Team
from ihalar.models import Iha

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_ihas = Iha.objects.order_by('-created_date').filter(is_featured = True)
    all_ihas = Iha.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'featured_ihas': featured_ihas,
        'all_ihas': all_ihas
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')