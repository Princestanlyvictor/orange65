# Generated by Django 3.1.6 on 2021-02-23 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_userdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.poductdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userdetail')),
            ],
        ),
    ]
