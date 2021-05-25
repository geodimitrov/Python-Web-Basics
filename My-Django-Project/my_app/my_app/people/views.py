from django.http import HttpResponse
from django.shortcuts import render

from my_app.people.models import Person


def index(request):
    context = {"Name": "Georgi"}
    return render(request, 'index.html', context)

def people_page(request):
    context = {
        "people": Person.objects.all(),
    }
    return render(request, 'people.html', context)