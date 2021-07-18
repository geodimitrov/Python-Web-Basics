from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = UserCreationForm()
    context = {
        'form': form,

    }
    return render(request, 'auth/sign_up.html', context)


def sign_in(request):
    pass


def sign_out(request):
    logout(request)
    return redirect('index.html')
