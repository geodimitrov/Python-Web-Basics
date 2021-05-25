from django.urls import path

from my_app.people.views import people_page

urlpatterns = [
    path('', people_page)
]