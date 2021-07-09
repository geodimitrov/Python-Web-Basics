from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


def create(request):
    if request.method == 'POST':
        form = PythonCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = PythonCreateForm()
    context = {
        'form': form,
    }

    return render(request, 'create.html', context)