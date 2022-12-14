# Generated by Django 4.1.3 on 2022-12-04 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess_club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='birthyear',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='firstname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='lastname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
