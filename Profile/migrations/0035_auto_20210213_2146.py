# Generated by Django 3.1.4 on 2021-02-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0034_points_of_interest_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to="{% url 'statesimg' %}"),
        ),
    ]
