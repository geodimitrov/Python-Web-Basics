from django.shortcuts import render


def homepage_view(request):
    context = {
    }
    return render(request, 'home.html', context)
