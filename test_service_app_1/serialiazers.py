from rest_framework import serializers
from .models import Company, CompanyManager, User, CompanyAdmin,Client

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'role','password')

class CompanyAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyAdmin
        fields = ('firstname', 'surname')

class CompanyManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyManager
        fields = ('firstname', 'surname','company_link')

class CompanyClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('firstname', 'surname')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields=('company_name','fio_otvetst','email_otvetst','phone_otvetst','business_id_number',
        'business_kpp','full_company_name','post_index','street','house_number','building',
        'office_number','bank_iik','raschet_schet','bank_name','correspondent_account','clients')