from django.shortcuts import render, redirect
from notes.common.notes_utils import get_profile, get_notes_count
from notes.note_manager.models import Note
from notes.profile_manager.forms import CreateProfileForm


def profile_details(request):
    context = {
        'notes_count': get_notes_count(),
        'profile': get_profile(),
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = CreateProfileForm()
    context = {'form': form}
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    profile.delete()
    Note.objects.all().delete()
    return redirect('home')