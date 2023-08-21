from django.shortcuts import render

# Create your views here.
def ihalar(request):
    return render(request, 'ihalar/ihalar.html')