# Generated by Django 2.2.10 on 2021-03-29 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210329_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poductdetails',
            name='available',
        ),
    ]
