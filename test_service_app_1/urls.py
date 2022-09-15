from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('advertapp', views.home_page, name='data_list'),
    path('login-form/login', views.loginform, name='loginform'),
    path('advertapp/register', views.register, name='register'),
    path('advertapp/register_manager', views.register_manager, name='register_manager'),
    path('logout', views.logout, name='logout'),
    path('facebook_api', views.facebook_api_req, name='facebook_api_req'),



    path('test', views.test_page, name='test'),
    path('test1', views.test_1, name='test1'),
    path('test2/<int:company_id>/<client_name>', views.test_2, name='test2'),
    path('user_list', views.user_list, name='user_list')
]