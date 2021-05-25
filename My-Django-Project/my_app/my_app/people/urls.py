from django.urls import path
from my_app.people.views import index

urlpatterns = [
    path('', index),
]