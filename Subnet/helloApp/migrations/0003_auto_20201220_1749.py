# Generated by Django 3.1.4 on 2020-12-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloApp', '0002_auto_20201220_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newexposure',
            name='new_sub_value',
            field=models.IntegerField(blank=True, null=True, verbose_name='Subnet Valuesss'),
        ),
    ]