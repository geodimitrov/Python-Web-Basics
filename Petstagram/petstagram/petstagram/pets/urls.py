from django.urls import path

from petstagram.pets.views import pet_all, pet_details, like_pet

urlpatterns = [
    path('', pet_all, name="all pets"),
    path('details/<int:id>', pet_details, name="pet details"),
    path('like/<int:id>', like_pet, name="like pet"),
]