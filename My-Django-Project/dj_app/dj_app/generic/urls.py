# generic.urls
from django.urls import path
from dj_app.generic.views import contact_page, index, about_page

urlpatterns = [
    path('', index),
    path('contact/', contact_page),
    path('about/', about_page),
]