# Generated by Django 3.1.4 on 2021-02-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_auto_20210202_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_city', models.CharField(max_length=50)),
                ('Name_of_airport', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'ordering': ('Name_of_city', 'Name_of_airport'),
            },
        ),
    ]
