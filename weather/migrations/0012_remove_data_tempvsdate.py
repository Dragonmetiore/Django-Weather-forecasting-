# Generated by Django 4.1 on 2022-11-20 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0011_alter_data_tempvsdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='TempVsDate',
        ),
    ]
