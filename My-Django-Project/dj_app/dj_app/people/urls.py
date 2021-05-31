from django.urls import path
from dj_app.people.views import people_page, create_person

urlpatterns = [
    path('', people_page),
    path('create/', create_person)
]