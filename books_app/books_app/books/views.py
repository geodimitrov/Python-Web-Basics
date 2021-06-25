from django.shortcuts import render, redirect
from books_app.books.forms import BookForm
from books_app.books.models import Book


def show_book_form(request, form, template_name):
    context = {
        'form': form
    }
    return render(request, template_name, context)


def create_book_from_form(request, form, template_name):
    if form.is_valid():
        form.save()
        return redirect('index page')

    return show_book_form(request, form, template_name)


def index(request):
    context = {
        "books": Book.objects.all(),
    }
    return render(request, 'index.html', context)


def create_book(request):
    template = 'create.html'

    if request.method == "GET":
        return show_book_form(request, BookForm(), template)

    else:
        form = BookForm(request.POST)
        return create_book_from_form(request, form, template)


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    template = 'edit.html'

    if request.method == "GET":
        form = BookForm(initial=book.__dict__)
        return show_book_form(request, form, template)

    else:
        form = BookForm(
            request.POST,
            instance=book,
        )
        return create_book_from_form(request, form, template)
