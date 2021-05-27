from django.urls import path

from my_app.cars.views import cars_page

urlpatterns = [
    path('', cars_page),
]