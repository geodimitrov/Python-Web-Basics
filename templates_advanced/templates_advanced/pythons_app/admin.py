from django.contrib import admin
from .models import Python


@admin.register(Python)
class PythonAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
