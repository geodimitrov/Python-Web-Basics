from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.note_manager.urls')),
    path('profile/', include('notes.profile_manager.urls')),
]
