from django.shortcuts import render, redirect

from expense_tracker.profiles.forms import ProfileForm


def profile_details(request):
    pass


def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProfileForm()

    context = {'form': form}
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    pass


def delete_profile(request):
    pass
