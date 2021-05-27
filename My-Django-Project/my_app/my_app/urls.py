from django.contrib import admin
from django.urls import path, include
from my_app.views import index
from my_app.views import contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact/', contact_page),
    path('people/', include("my_app.people.urls")),
    path('cars/', include("my_app.cars.urls")),
]
