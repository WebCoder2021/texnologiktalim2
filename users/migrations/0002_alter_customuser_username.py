# Generated by Django 4.1.3 on 2022-12-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=200, unique=True, verbose_name='Username'),
        ),
    ]
