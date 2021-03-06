# Generated by Django 3.1.4 on 2020-12-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddSubList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_subnet_name', models.CharField(max_length=255, verbose_name='Subnet Name')),
                ('acc_subnet_value', models.IntegerField(verbose_name='Subnet Value')),
            ],
            options={
                'verbose_name': 'AddSubList',
                'verbose_name_plural': 'AddSubLists',
            },
        ),
        migrations.CreateModel(
            name='NetworkList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subnet_name', models.CharField(max_length=255, verbose_name='Subnet Name')),
                ('subnet_value', models.IntegerField(verbose_name='Subnet Value')),
            ],
            options={
                'verbose_name': 'NetworkList',
                'verbose_name_plural': 'NetworkLists',
            },
        ),
    ]
