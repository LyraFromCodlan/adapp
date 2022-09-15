from http import client
import requests
import json

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate,login,logout as django_logout

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import User, Client, Company
from .serialiazers import UserSerializer
from .forms import CompanyForm, RegisterAdminForm,RegisterUserForm,LoginForm,ClientForm



from django.contrib.auth.decorators import login_required
# from rest_framework import viewsets
# from rest_framework import permissions
# from django.contrib.auth.models import Group
# from django.views.generic import CreateView
# from test_service_app_1.serialiazers import UserSerializer


# Create your views here.

def home_page(request):
    
    return render(request, 'test_service_app_1/home.html', {})

def data_list_objects(request):
    return render(request, 'test_service_app_1/home.html', {})


@api_view(['GET','POST'])
def companyDetailForm(request):
    form=CompanyForm(data=request.POST)
    if request.method=="POST":
        print(request.POST)
        if form.is_valid():
            print('\nForm is valid\n')
            form.save()
            return HttpResponseRedirect('')
        else:
            print('\nForm is not valid\n')
    else:
        pass
        # endpoint=""
        
        # get_resp = requests.get(endpoint,params={}, json={})
    return render(request,'test_service_app_1/companyDetail.html',{'companyDetailForm':form})

@api_view(['GET','POST'])
def loginform(request):
    form = LoginForm(data=request.POST)
    if request.method=="POST":
        print(request.POST) 
        if form.is_valid():
            print("\nForm is valid\n")
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
        else:
            print("\nForm is not valid\n")
    else:
        pass
        
        
    return render(request, 'test_service_app_1/login.html', {'log_form': form})


@api_view(['GET','POST'])
def register(request):
    form = RegisterAdminForm(data=request.POST)
    if request.method=="POST":
        print(request.POST)
        if form.is_valid():
            print("\nForm is valid\n")
            # process the data in form.cleaned_data as required
            user = form.save(commit=False)
            user.save()
            username=form.cleaned_data.get('email')
            raw_password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            # redirect to a new URL:
            return HttpResponseRedirect('')
        else:
            print("\nForm is not valid\n")
    else:
        pass
        # endpoint=""
        
        # get_resp = requests.get(endpoint,params={}, json={})
        
    return render(request, 'test_service_app_1/registration.html', {'reg_form': form})


@api_view(['GET','POST'])
def register_manager(request):


    form = RegisterUserForm(data=request.POST)
    if request.method=="POST":
        print(request.POST)
        if form.is_valid():
            print("\nForm is valid\n")
            user=form.save(commit=False)
            user.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')
        else:
            print("\nForm is not valid\n")
    else:
        pass
        # endpoint=""
        
        # get_resp = requests.get(endpoint,params={}, json={})

        
    return render(request, 'test_service_app_1/registration.html', {'reg_form': form})

@login_required(login_url="login-form/login")
@api_view(['GET','POST'])
def logout(request):
    if request.method == 'GET':
        return render(request, 'test_service_app_1/logout.html')
    if request.method == 'POST':
        django_logout(request)
        form = LoginForm(data=request.POST)
        return redirect('login-form/login')
        # return render(request, 'test_service_app_1/login.html', {'log_form': form},status=status.HTTP_202_ACCEPTED)

@login_required(login_url="facebook_api")
@api_view(['GET'])
def facebook_api_req(request):
    return JsonResponse({"user_list":"data"}, safe = False)








def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many = True)
        return JsonResponse({"user_list":user_serializer.data}, safe = False)
    if request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            print('data is valid')
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


def test_page(request, *args,**kwargs):

    print("\nResponse data:\n")
    print("Whole data:")
    print(request.GET)
    print("\nheaders:")
    print(request.headers)
    print("\ncontent-type:")
    print(request.content_type)
    endpoint="http://127.0.0.1:8000/test1"

    get_resp = requests.get(endpoint)

    body = json.loads(get_resp.text)
    print(body)
    return JsonResponse({"data":"Data from json","rest data":{"json_value":body}})

def test_1(request):
    return JsonResponse({"test_1":"Test_1 response data"})

@api_view(['GET','POST'])
def test_2(request, company_id,client_name):
    form = ClientForm(data=request.POST)
    if request.method=="POST":
        print(request.POST)
        if form.is_valid():
            pass
            # print("\nForm is valid\n")
            # # process the data in form.cleaned_data as required
            # user = form.save(commit=False)
            # user.save()
            # username=form.cleaned_data.get('email')
            # raw_password=form.cleaned_data.get('password')
            # user=authenticate(username=username,password=raw_password)
            # login(request,user)
            # # redirect to a new URL:
            # return HttpResponseRedirect('')
        else:
            print("\nForm is not valid\n")
    else:
        pass
        # endpoint=""
        
        # get_resp = requests.get(endpoint,params={}, json={})
        
    




    # client = Client()
    # company = Company.objects.get(company_id=company_id)
    # client.company_id = company
    # client.client_name = client_name
    # client.save()
    # return JsonResponse({"Company data":str(company_id)+", "+client_name})
    return render(request, 'test_service_app_1/registration.html', {'reg_form': form})

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]