from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('advertapp', views.home_page, name='data_list'),
    path('advertapp/login', views.login, name='login'),
    path('advertapp/register', views.register, name='register'),
    path('advertapp/register_manager', views.register_manager, name='register_manager'),
]