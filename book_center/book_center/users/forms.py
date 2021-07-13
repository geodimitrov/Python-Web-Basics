from django.forms import ModelForm

from book_center.users.models import TestCreateUser


class CreateUserForm(ModelForm):
    class Meta:
        model = TestCreateUser
        fields = '__all__'
