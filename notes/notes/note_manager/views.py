from django.shortcuts import render, redirect
from notes.common.notes_utils import get_note
from notes.note_manager.forms import NoteForm, DeleteNoteForm
from notes.note_manager.models import Note
from notes.profile_manager.models import Profile
from notes.profile_manager.views import create_profile


def home_page(request):
    profile = Profile.objects.first()

    if not profile:
        return create_profile(request)

    context = {'notes': Note.objects.all()}
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()

    context = {'form': form}
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = get_note(pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)

    context = {'note': note, 'form': form}
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = get_note(pk)

    if request.method == 'POST':
        note.delete()
        return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)

    context = {'note': note, 'form': form}
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = get_note(pk)
    context = {'note': note}
    return render(request, 'note-details.html', context)