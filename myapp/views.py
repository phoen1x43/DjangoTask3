from django.http import HttpResponse
from .models import Message
from django.utils import timezone

def hello(request, name):
    Message.objects.create(name=name)
    return HttpResponse(f"Hello, {name}!")

def stats(request):
    count = Message.objects.count()
    return HttpResponse(f"Total greetings: {count}")

def stats_name(request, name):
    messages = Message.objects.filter(name=name).order_by('-created_at')
    response = f"Greeting history for {name}:<br>"
    response += "<br>".join(timezone.localtime(m.created_at).strftime('%Y-%m-%d %H:%M:%S') for m in messages)
    return HttpResponse(response)
