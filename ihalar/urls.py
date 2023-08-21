
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ihalar, name='ihalar'),

]
