from django.urls import path
from todo_app.todos.views import index, create_todo

urlpatterns = [
    path('', index),
    path('create-todo/', create_todo),
]