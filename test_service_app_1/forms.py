#from msilib.schema import Class
from attr import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from test_service_app_1 import models

from test_service_app_1.models import Company, CompanyAdmin, CompanyManager, User, Client

class RegisterAdminForm(UserCreationForm):
    #password=forms.CharField(widget=forms.PasswordInput)
    class Meta(UserCreationForm):
        model=CompanyAdmin
        fields=('username','first_name','surname','role')

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',)

class RegisterUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CompanyManager
        fields=('username','first_name','surname','role')



class LoginForm(forms.Form):
    username=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=('company_name','fio_otvetst','email_otvetst','phone_otvetst','business_id_number',
        'business_kpp','full_company_name','post_index','street','house_number','building',
        'office_number','bank_iik','raschet_schet','bank_name','correspondent_account',)

class ClientForm(UserCreationForm):

    class Meta(UserCreationForm):
        name=Client
        fields=('client_name','company_id','has_vk','has_fb','has_google','has_yandex','has_myTarget','has_tiktok')