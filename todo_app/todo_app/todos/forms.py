from django import forms
from django.core.validators import MinValueValidator, MinLengthValidator


def validate_dot(value):
    if "." in value:
        raise forms.ValidationError("You cannot have '.' in the input")

class CreateTodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=[
            validate_dot,
            MinLengthValidator(3),
        ]
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter text"
            }
        )
    )
    # state = forms.BooleanField()