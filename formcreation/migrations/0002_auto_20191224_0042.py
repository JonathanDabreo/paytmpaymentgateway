# Generated by Django 3.0 on 2019-12-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formcreation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_of_user',
            name='amount',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='data_of_user',
            name='address',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='data_of_user',
            name='semester',
            field=models.IntegerField(max_length=200),
        ),
    ]
