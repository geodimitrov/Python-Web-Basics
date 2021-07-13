from django.shortcuts import render
from book_center.users.forms import CreateUserForm


def register_user_view(request):
    form = CreateUserForm()
    context = {
        'form': form,
    }

    return render(request, 'users/user_registration.html', context)