from django.shortcuts import render, redirect
from books_app.books.forms import BookForm
from books_app.books.models import Book


def index(request):
    context = {
        "books": Book.objects.all(),
    }
    return render(request, 'index.html', context)


def create_book(request):
    if request.method == "GET":
        context = {
            'form': BookForm()
        }
        return render(request, 'create.html', context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index page')

        context = {
            'form': BookForm()
        }
        return render(request, 'create.html', context)



def update_book(request, pk):
    if request.method == "GET":
        pass
    else:
        pass
