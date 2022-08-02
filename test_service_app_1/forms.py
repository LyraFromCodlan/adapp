from msilib.schema import Class
from attr import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm

from test_service_app_1.models import User

class RegisterAdminForm(forms.Form):
    ROLES=(
            (1,"Admin"),
            (2,"CompanyAdmin"),
            (3,"CompanyManager"),
        )

    email = forms.EmailField(label='email', max_length=50,initial='something@gmail.com', required=True)
    first_name = forms.CharField(label='Имя', max_length=50)
    surname = forms.CharField(label='Фамилия', max_length=50)
    password = forms.CharField(label="password",max_length=50, required=True,widget=forms.PasswordInput)
    approve_password = forms.CharField(label="approve_password",max_length=50, required=True,widget=forms.PasswordInput)
    role = forms.ChoiceField(label="Role",choices=ROLES ,help_text="You must choose one of the roles in the list", required=True)

class RegisterUserForm(forms.Form):
    ROLES=(
        (1,"Admin"),
        (2,"CompanyAdmin"),
        (3,"CompanyManager"),
    )

    email = forms.EmailField(label='email', max_length=50,initial='something@gmail.com', required=True)
    first_name = forms.CharField(label='Имя', max_length=50)
    surname = forms.CharField(label='Фамилия', max_length=50)
    password = forms.CharField(label="password",max_length=50, required=True,widget=forms.PasswordInput)
    approve_password = forms.CharField(label="approve_password",max_length=50, required=True,widget=forms.PasswordInput)
    role = forms.ChoiceField(label="Role",choices=ROLES ,help_text="You must choose one of the roles in the list", required=True)


class LoginForm(forms.Form):
    ROLES=(
        (1,"Admin"),
        (2,"CompanyAdmin"),
        (3,"CompanyManager"),
    )

    email = forms.EmailField(label='email', max_length=50,initial='something@gmail.com', required=True)
    password = forms.CharField(label="password",max_length=50, required=True,widget=forms.PasswordInput)
    role = forms.ChoiceField(label="Role",choices=ROLES ,help_text="You must choose one of the roles in the list", required=True)
