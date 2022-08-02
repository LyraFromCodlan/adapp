from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.views.generic import CreateView
from .forms import RegisterAdminForm,RegisterUserForm,LoginForm

# Create your views here.

def home_page(request):
    
    return render(request, 'test_service_app_1/home.html', {})

def data_list_objects(request):
    return render(request, 'test_service_app_1/home.html', {})

def login(request):
    form = LoginForm(data=request.POST)
    if request.method=="POST":
        print(request.POST) 
        if form.is_valid():
            print("\nForm is valid\n")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')
        else:
            print("\nForm is not valid\n")
        
    return render(request, 'test_service_app_1/login.html', {'log_form': form})

def register(request):
    form = RegisterAdminForm(data=request.POST)
    if request.method=="POST":
        print(request.POST)
        if form.is_valid():
            print("\nForm is valid\n")
            # process the data in form.cleaned_data as required
            user = form.save(commit=False)
            user.save()
            # redirect to a new URL:
            return HttpResponseRedirect('')
        else:
            print("\nForm is not valid\n")
        
    return render(request, 'test_service_app_1/registration.html', {'reg_form': form})

def register_manager(request):
    form = RegisterUserForm(data=request.POST)
    if request.method=="POST":
        print(request.POST)
        if form.is_valid():
            print("\nForm is valid\n")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')
        else:
            print("\nForm is not valid\n")
        
    return render(request, 'test_service_app_1/registration.html', {'reg_form': form})