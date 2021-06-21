# Generated by Django 3.1.4 on 2021-02-13 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0025_auto_20210213_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightbookingshistory',
            name='bookingid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.userprofile'),
        ),
        migrations.AddField(
            model_name='flightbookingshistory',
            name='category',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='flightbookingshistory',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='flightbookingshistory',
            name='journey',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='flightbookingshistory',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
    ]
