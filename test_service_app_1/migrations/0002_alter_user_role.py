# Generated by Django 4.0.6 on 2022-08-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_service_app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'CompanyAdmin'), (3, 'CompanyManager')], default='', max_length=20, verbose_name='Роль'),
        ),
    ]
