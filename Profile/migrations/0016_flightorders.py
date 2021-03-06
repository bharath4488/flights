# Generated by Django 3.1.4 on 2021-02-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0015_user_querie'),
    ]

    operations = [
        migrations.CreateModel(
            name='flightorders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('adults', models.CharField(max_length=50)),
                ('children', models.CharField(max_length=50)),
                ('dsitance', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(default=1)),
                ('datetime', models.CharField(max_length=50)),
                ('classtype', models.CharField(max_length=10)),
            ],
        ),
    ]
