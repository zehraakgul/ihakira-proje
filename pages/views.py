from django.shortcuts import render
from .models import Team
from ihalar.models import Iha

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_ihas = Iha.objects.order_by('-created_date').filter(is_featured = True)
    all_ihas = Iha.objects.order_by('-created_date')
    #search_fields = Iha.objects.values('model', 'city', 'year', 'condition')
    model_search = Iha.objects.values_list('model', flat=True).distinct()
    city_search = Iha.objects.values_list('city', flat=True).distinct()
    year_search = Iha.objects.values_list('year', flat=True).distinct()
    condition_search = Iha.objects.values_list('condition', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_ihas': featured_ihas,
        'all_ihas': all_ihas,
        #'search_fields': search_fields,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'condition_search': condition_search,

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