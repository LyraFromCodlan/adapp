import email
from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):


    ROLES=(
        (1,"Admin"),
        (2,"CompanyAdmin"),
        (3,"CompanyManager"),
    )

    role = models.IntegerField('Роль', default='', choices=ROLES)
    position = models.CharField('Назначение клиентов',max_length=50, default='',null=True,blank=True)

    def create_user(self, username, password, email):
        user = self.model(
            email=email,
            password=password,
            username=username
        )
        
class Company(models.Model):
    client_id = models.CharField(max_length=50, default='', unique=True)
    token = models.CharField(max_length=100, default='', unique=True)

class Facebook(models.Model):
    client_id = models.CharField(max_length=50, default='', unique=True)
    token = models.CharField(max_length=100, default='', unique=True)
    login = models.CharField(max_length=50, default='', unique=True)
    password = models.CharField(max_length=50, default='', unique=True)

class VK(models.Model):
    client_id = models.CharField(max_length=50, default='', unique=True)
    token = models.CharField(max_length=100, default='', unique=True)
    version = models.CharField(max_length=100, default='', unique=True)
    id_rk = models.CharField(max_length=100, default='', unique=True)

class Google(models.Model):
    client_id = models.CharField(max_length=50, default='', unique=True)
    developer_token = models.CharField(max_length=100, default='', unique=True)
    gclient_id = models.CharField(max_length=50, default='', unique=True)
    client_secret = models.CharField(max_length=50, default='', unique=True)
    refresh_token = models.CharField(max_length=100, default='', unique=True)
    login_customer_id = models.CharField(max_length=50, default='', unique=True)
    login = models.CharField(max_length=50, default='', unique=True)
    password = models.CharField(max_length=50, default='', unique=True)

class Yandex(models.Model):
    client_id = models.CharField(max_length=50, default='', unique=True)
    token = models.CharField(max_length=100, default='', unique=True)
    client_login = models.CharField(max_length=50, default='', unique=True)

class TikTok(models.Model):
    client_id = models.CharField(max_length=50, default='', unique=True)
    access_token = models.CharField(max_length=100, default='', unique=True)
    refresh_token = models.CharField(max_length=100, default='', unique=True)
    client_key = models.CharField(max_length=100, default='', unique=True)
    client_secret = models.CharField(max_length=100, default='', unique=True)

class MyTarget(models.Model):
    client_id = models.CharField(max_length=50, default='', unique=True)
    mclient_id = models.CharField(max_length=50, default='', unique=True)
    client_secret = models.CharField(max_length=100, default='', unique=True)
    token = models.CharField(max_length=100, default='', unique=True)
    refresh_token = models.CharField(max_length=100, default='', unique=True)





class Client(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField('',max_length=50, default='')
    company_id = models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
    has_vk = models.ForeignKey(VK, default=None, on_delete=models.CASCADE)
    has_fb = models.ForeignKey(Facebook, default=None, on_delete=models.CASCADE)
    has_google = models.ForeignKey(Google, default=None, on_delete=models.CASCADE)
    has_yandex = models.ForeignKey(Yandex, default=None, on_delete=models.CASCADE)
    has_myTarget = models.ForeignKey(MyTarget, default=None, on_delete=models.CASCADE)
    has_tiktok = models.ForeignKey(TikTok, default=None, on_delete=models.CASCADE)













class AddServiceData(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service_user_name = models.CharField(max_length=200)
    info = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.service_user_name