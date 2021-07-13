from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_center.common.urls')),
    path('users/', include('book_center.users.urls')),
]
