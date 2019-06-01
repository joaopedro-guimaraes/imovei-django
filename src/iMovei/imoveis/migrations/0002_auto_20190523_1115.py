# Generated by Django 2.2.1 on 2019-05-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='bairro',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='imovel',
            name='cep',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='imovel',
            name='cidade',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='imovel',
            name='complemento',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='imovel',
            name='estado',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='imovel',
            name='numero',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imovel',
            name='rua',
            field=models.CharField(default='', max_length=50),
        ),
    ]
