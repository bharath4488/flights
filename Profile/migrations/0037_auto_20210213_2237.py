# Generated by Django 3.1.4 on 2021-02-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0036_auto_20210213_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points_of_interest',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='POIs'),
        ),
        migrations.AlterField(
            model_name='state',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='statesimg'),
        ),
    ]
