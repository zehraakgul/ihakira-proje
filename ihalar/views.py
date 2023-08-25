from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ihalar.models import Iha


# Create your views here.
def ihalar(request):
    ihalar = Iha.objects.order_by('-created_date')
    paginator = Paginator(ihalar,4)
    page = request.GET.get('page')
    paged_ihalar = paginator.get_page(page)

    model_search = Iha.objects.values_list('model', flat=True).distinct()
    city_search = Iha.objects.values_list('city', flat=True).distinct()
    year_search = Iha.objects.values_list('year', flat=True).distinct()
    condition_search = Iha.objects.values_list('condition', flat=True).distinct()

    data = {
        'ihalar': paged_ihalar,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'condition_search': condition_search,
    }
    return render(request, 'ihalar/ihalar.html', data)

def iha_detail(request, id):
    single_iha = get_object_or_404(Iha, pk = id)
    data = {
        'single_iha': single_iha,
    }
    return render(request, 'ihalar/iha_detail.html', data)

def search(request):
    ihalar = Iha.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            ihalar = ihalar.filter(description__icontains = keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            ihalar = ihalar.filter(model__iexact = model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            ihalar = ihalar.filter(city__iexact = city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            ihalar = ihalar.filter(year__iexact = year)

    if 'condition' in request.GET:
        condition = request.GET['condition']
        if condition:
            ihalar = ihalar.filter(condition__iexact = condition)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            ihalar = ihalar.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'ihalar': ihalar,
    }
    return render(request, 'ihalar/search.html', data)