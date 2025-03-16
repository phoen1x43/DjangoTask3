from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

def hello(request, name):
    Message.objects.create(name=name)
    return render(request, "welcome.html", {"name": name})

def stats(request):
    total_greetings = Message.objects.count()
    return render(request, "stats.html", {"total_greetings": total_greetings})

def stats_name(request, name):
    greetings = Message.objects.filter(name=name).order_by('-timestamp')
    return render(request, "stats_name.html", {"name": name, "greetings": greetings})

