# Generated by Django 4.1 on 2022-11-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0022_data_conditionvsdate_data_tempvsdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='ConditionVsDate',
            field=models.ImageField(default='Sorry Some Error occur', upload_to='weather/images'),
        ),
        migrations.AlterField(
            model_name='data',
            name='TempVsDate',
            field=models.ImageField(default='Sorry Some Error occur', upload_to='weather/images'),
        ),
    ]
