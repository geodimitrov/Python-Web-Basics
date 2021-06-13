from django.shortcuts import render, redirect

from petstagram.pets.models import Pet, Like


def pet_all(request):
    context = {
        "pets": Pet.objects.all(),
    }

    return render(request, 'pets/pet_list.html', context)


def pet_details(request, id):
    context = {
        "pet": Pet.objects.get(pk=id),
    }
    return render(request, 'pets/pet_detail.html', context)

def like_pet(request, id):
    pet_to_like = Pet.objects.get(pk=id)
    like = Like(
        pet=pet_to_like
    )
    like.save()
    return redirect('pet details', pet_to_like.id)
