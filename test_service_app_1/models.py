import email
from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

# Create your models here.



ROLES=(
    (1,"Admin"),
    (2,"CompanyAdmin"),
    (3,"CompanyManager"),
    
)

# Добавить разграничение при регистрации роли!! Админ рекламного агентства не должен регистрировтаь обычных админов!


class User(AbstractUser):
    username=models.EmailField('email', max_length=50,default='',unique=True)
    role = models.IntegerField('Роль', default=1, choices=ROLES)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]

    # class Meta:
    #     db_table = "users"
        # verbose_name="Пользователь"
        # verbose_name_plural="Пользователи"

    def create_user(self, username, password, email):
        user = self.model(
            email=email,
            password=password,
            username=username
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user=self.create_user(username=username, password=password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.role=1
        user.save(using=self._db)
        return user
        
class CompanyAdmin(User):
    firstname = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)

    # class Meta:
    #     db_table = "companys_admin"
    



class Company(models.Model):
    company_admin=models.ForeignKey(settings.AUTH_USER_MODEL,default='',on_delete=models.CASCADE)
    company_id=models.AutoField(primary_key=True)
    company_name=models.CharField('Наименование организации',max_length=255,default='')
    fio_otvetst=models.CharField('ФИО ответственного лица',max_length=255,default='')
    email_otvetst=models.EmailField('E-mail ответственного лица')
    phone_otvetst=models.CharField('Телефон ответственного лица',max_length=255,default='')
    business_id_number=models.IntegerField('БИН',default=0)
    business_kpp=models.CharField('КПП',max_length=255,default='')
    full_company_name=models.CharField('Полное наименование организации',max_length=255,default='')
    post_index=models.IntegerField('Почтовый индекс',default=0)
    street=models.CharField('Улица',max_length=255,default='')
    house_number=models.CharField('Номер дома', max_length=255,default='')
    building=models.CharField('Корпус',max_length=255,default='')
    office_number=models.CharField('Номер офиса',max_length=255,default='')
    bank_iik=models.CharField('БИК', max_length=255,default='')
    raschet_schet=models.CharField('Расчетный счет',max_length=255,default='')
    bank_name=models.CharField('Название банка',max_length=255,default='')
    correspondent_account=models.CharField('Корреспондентный счет',max_length=255,default='')

    # class Meta:
    #     db_table = "companies"

    def __str__(self):
        return self.company_name

class CompanyManager(User):
    firstname = models.CharField('Имя',default='', max_length=50)
    surname = models.CharField('Фамилия',default='', max_length=50)
    company_link=models.ForeignKey(Company,verbose_name='Рекламное агентство',blank=True, null=True, on_delete=models.SET_NULL)

    # class Meta:
    #     db_table = "companys_managers"
class Client(models.Model):

    USERNAME_FIELD='client_name'
    REQUIRED_FIELDS=['client_name','company_id']

    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField('Имя клиента',max_length=50)
    company_id = models.ForeignKey(Company, default=None,blank=True, null=True, on_delete=models.SET_NULL)
    has_vk = models.BooleanField(default=None, blank=True, null=True)
    has_fb = models.BooleanField(default=None, blank=True, null=True)
    has_google = models.BooleanField(default=None, blank=True, null=True)
    has_yandex = models.BooleanField(default=None, blank=True, null=True)
    has_myTarget = models.BooleanField(default=None, blank=True, null=True)
    has_tiktok = models.BooleanField(default=None, blank=True, null=True)

    # class Meta:
    #     db_table = "companys_clients"

    # def create_client(self, client_name, company_id):
    #     client = self.model(
    #         client_name = client_name,
    #         company_id = company_id
    #     )
    #     client.save(using=self._db)
    #     return client

    # def __str__(self):
    #     return 'Client: '+str(self.client_name)+", Ads Agency: "+self.company_id

class Facebook(models.Model):
    client_id = models.ForeignKey(Client,blank=True, null=True,on_delete=models.SET_NULL)
    token = models.CharField(max_length=100, default='', unique=True)
    login = models.CharField(max_length=50, default='', unique=True)
    password = models.CharField(max_length=50, default='', unique=True)

    # class Meta:
    #     db_table = "facebook_data"

class VK(models.Model):
    client_id = models.ForeignKey(Client,blank=True, null=True,on_delete=models.SET_NULL)
    token = models.CharField(max_length=100, default='', unique=True)
    version = models.CharField(max_length=100, default='', unique=True)
    id_rk = models.CharField(max_length=100, default='', unique=True)

    # class Meta:
    #     db_table = "vk_data"

class Google(models.Model):
    client_id = models.ForeignKey(Client,blank=True, null=True,on_delete=models.SET_NULL)
    developer_token = models.CharField(max_length=100, default='', unique=True)
    gclient_id = models.CharField(max_length=50, default='', unique=True)
    client_secret = models.CharField(max_length=50, default='', unique=True)
    refresh_token = models.CharField(max_length=100, default='', unique=True)
    login_customer_id = models.CharField(max_length=50, default='', unique=True)
    login = models.CharField(max_length=50, default='', unique=True)
    password = models.CharField(max_length=50, default='', unique=True)
    # class Meta:
    #     db_table = "google_data"

class Yandex(models.Model):
    client_id = models.ForeignKey(Client,blank=True, null=True,on_delete=models.SET_NULL)
    token = models.CharField(max_length=100, default='', unique=True)
    client_login = models.CharField(max_length=50, default='', unique=True)
    # class Meta:
    #     db_table = "yandex_data"

class TikTok(models.Model):
    client_id = models.ForeignKey(Client,blank=True, null=True,on_delete=models.SET_NULL)
    access_token = models.CharField(max_length=100, default='', unique=True)
    refresh_token = models.CharField(max_length=100, default='', unique=True)
    client_key = models.CharField(max_length=100, default='', unique=True)
    client_secret = models.CharField(max_length=100, default='', unique=True)
    # class Meta:
    #     db_table = "tiktok_data"

class MyTarget(models.Model):
    client_id = models.ForeignKey(Client,blank=True, null=True,on_delete=models.SET_NULL)
    mclient_id = models.CharField(max_length=50, default='', unique=True)
    client_secret = models.CharField(max_length=100, default='', unique=True)
    token = models.CharField(max_length=100, default='', unique=True)
    refresh_token = models.CharField(max_length=100, default='', unique=True)
    # class Meta:
    #     db_table = "my_target_data"

















