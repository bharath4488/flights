# Generated by Django 3.1.4 on 2021-02-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0040_state_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='points_of_interest',
            name='slug',
            field=models.SlugField(default='state', max_length=100),
        ),
    ]
