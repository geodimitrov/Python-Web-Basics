from django.shortcuts import render, redirect
from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet, Like


def show_pet_form(request, form, template_name):
    context = {
        'form': form
    }
    return render(request, template_name, context)


def pet_all(request):
    context = {
        "pets": Pet.objects.all(),
    }

    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    context = {
        "pet": Pet.objects.get(pk=pk),
    }
    return render(request, 'pets/pet_detail.html', context)


def like_pet(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet_to_like
    )
    like.save()
    return redirect('pet details', pet_to_like.id)


def create_pet(request):
    if request.method == "GET":
        return show_pet_form(request, PetForm(), 'pets/pet_create.html')
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all pets')

    return show_pet_form(request, PetForm(), 'pets/pet_create.html')


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == "GET":
        form = PetForm(
                instance=pet
            )
        return show_pet_form(request, form, 'pets/pet_edit.html')

    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', pet.id)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    context = {
        'pet': pet
    }

    if request.method == "GET":
        return render(request, 'pets/pet_delete.html', context)
    else:
        pet.delete()
        return redirect('all pets')