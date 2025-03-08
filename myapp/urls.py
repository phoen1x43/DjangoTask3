from django.urls import path
from .views import hello, stats, stats_name

urlpatterns = [
    path('hello/<str:name>/', hello, name='hello'),
    path('stats/', stats, name='stats'),
    path('stats/<str:name>/', stats_name, name='stats_name'),
]