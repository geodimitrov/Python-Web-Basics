from django.contrib import admin
from todo_app.todos.models import Todo, Person


class TodoAdmin(admin.ModelAdmin):
    list_display = ['text', 'state']

admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
