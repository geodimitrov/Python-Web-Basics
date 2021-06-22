from django.shortcuts import render, redirect
from todo_app.todos.forms import CreateTodoForm
from todo_app.todos.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
        'form': CreateTodoForm()
    }

    return render(request, 'index.html', context)


def create_todo(request):
    # return render(request, 'create_todo_test_input.html')
    # text = request.POST['text']
    # description = request.POST['description']
    form = CreateTodoForm(request.POST)

    if form.is_valid():
        text = form.cleaned_data['text']
        description = form.cleaned_data['description']
        todo = Todo(
            text=text,
            description=description,
        )
        todo.save()
        return redirect('/')
    else:
        context = {
            'todos': Todo.objects.all(),
            'form': form,
        }

        return render(request, 'index.html', context)