from django.contrib import admin
from .models import  CompanyAdmin, User, Company, Facebook, VK, Google, Yandex, TikTok, MyTarget,Client
# Register your models here.
from .forms import *
from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = User
#     list_display = ['email','username']

admin.site.register(User)
admin.site.register(CompanyAdmin)
admin.site.register(Company)
admin.site.register(Facebook)
admin.site.register(VK)
admin.site.register(Google)
admin.site.register(Yandex)
admin.site.register(TikTok)
admin.site.register(MyTarget)
admin.site.register(Client)