from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.name_form, name='name_form'),
    path('stats/<str:name>/', views.stats_name, name='stats_name'),
]
