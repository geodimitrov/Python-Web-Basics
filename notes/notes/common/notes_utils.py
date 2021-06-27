from notes.note_manager.models import Note
from notes.profile_manager.models import Profile


def get_note(pk):
    return Note.objects.get(pk=pk)


def get_notes_count():
    return Note.objects.count()


def get_profile():
    return Profile.objects.first()




