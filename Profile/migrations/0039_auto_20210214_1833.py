# Generated by Django 3.1.4 on 2021-02-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0038_auto_20210214_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points_of_interest',
            name='Entry_fees_Adults',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='points_of_interest',
            name='Entry_fees_Children',
            field=models.CharField(default='', max_length=50),
        ),
    ]
