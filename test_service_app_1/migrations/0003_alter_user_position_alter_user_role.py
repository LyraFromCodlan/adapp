# Generated by Django 4.0.6 on 2022-08-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_service_app_1', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Назначение клиентов'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'CompanyAdmin'), (3, 'CompanyManager')], default='', verbose_name='Роль'),
        ),
    ]
