from django.shortcuts import render

from my_app.cars.models import Car


def cars_page(request):
    context = {
        "cars": Car.objects.all()
    }
    return render(request, 'cars.html', context)
