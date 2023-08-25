
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ihalar, name='ihalar'),
    path('<int:id>', views.iha_detail, name='iha_detail'),
    path('search', views.search, name = 'search'),

]
