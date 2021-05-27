from django.contrib import admin
from django.urls import path, include
from dj_app.views import index, contact_page, about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact/', contact_page),
    path('about/', about_page),
    path('people/', include('dj_app.people.urls'))
]
