from django.urls import path

from notes.profile_manager.views import profile_details, delete_profile, create_profile

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('delete/', delete_profile, name='delete profile'),
]