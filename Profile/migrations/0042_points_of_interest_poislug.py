# Generated by Django 3.1.4 on 2021-02-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0041_points_of_interest_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='points_of_interest',
            name='poislug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]