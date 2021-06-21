from django import forms


class CreateTodoForm(forms.Form):
    text = forms.CharField(max_length=30)
    description = forms.CharField(max_length=50)
    # state = forms.BooleanField()