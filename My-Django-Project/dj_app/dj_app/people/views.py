from django.shortcuts import render

from dj_app.people.models import Person


def people_page(request):
    context = {
        "people": Person.objects.all()
    }
    return render(request, "people.html", context)
