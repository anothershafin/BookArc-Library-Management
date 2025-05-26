from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
    librarian_code = forms.CharField(required=False, max_length=4)

    class Meta:
        model = CustomUser
        fields = [
            'username','first_name','last_name',
            'email','phone_number','role','librarian_code',
            'password1','password2'
        ]
