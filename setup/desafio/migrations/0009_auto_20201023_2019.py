# Generated by Django 3.1.2 on 2020-10-23 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio', '0008_auto_20201023_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rota',
            name='distancia',
            field=models.PositiveIntegerField(),
        ),
    ]
