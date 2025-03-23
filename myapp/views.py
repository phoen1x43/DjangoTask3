from django.shortcuts import render
from .models import Message
from .forms import NameForm

def home(request):
    total = Message.objects.count()
    users = Message.objects.values_list("name", flat=True).distinct()
    return render(request, "home.html", {
        "total": total,
        "users": users,
    })

def name_form(request):
    form = NameForm()
    name = None
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            Message.objects.create(name=name)
    return render(request, "form.html", {"form": form, "name": name})

def stats_name(request, name):
    greetings = Message.objects.filter(name=name).order_by("-timestamp")
    return render(request, "stats_name.html", {"name": name, "greetings": greetings})




