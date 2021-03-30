# Generated by Django 2.2.10 on 2021-03-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210311_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='poductdetails',
            name='category',
            field=models.CharField(blank=True, choices=[['stationery', 'Stationery'], ['vegetable', 'Vegtables/Fruits'], ['pantry', 'Pantry'], ['personalcare', 'Personalcare'], ['cleaning', 'Cleaning'], ['beverges', 'Beverges'], ['packagedfood', 'Packagedfood'], ['cookingessential', 'Cookingessential'], ['topoffer', 'Topoffer'], ['todaydeal', 'Todaydeal']], max_length=17, null=True),
        ),
    ]
