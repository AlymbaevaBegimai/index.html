# Generated by Django 3.1.3 on 2021-01-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210118_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('заголовок', models.CharField(max_length=100)),
                ('подзаголовок', models.CharField(max_length=80)),
                ('описание', models.CharField(max_length=700)),
                ('цена', models.IntegerField(max_length=50)),
                ('жанр', models.CharField(max_length=50)),
                ('автор', models.CharField(max_length=50)),
                ('год', models.DateField(max_length=50)),
                ('дата', models.DateField(auto_now_add=True)),
            ],
        ),
    ]