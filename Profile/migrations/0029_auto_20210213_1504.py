# Generated by Django 3.1.4 on 2021-02-13 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0028_auto_20210213_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightbookingshistory',
            name='bookingid',
        ),
        migrations.AddField(
            model_name='flightbookingshistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.userprofile'),
        ),
    ]
