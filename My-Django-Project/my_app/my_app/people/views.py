from django.shortcuts import render
from my_app.people.models import Person


def people_page(request):
    context = {
        "people": Person.objects.all(),
    }

    context["message"] = "Peoples' names"
    return render(request, 'people.html', context)