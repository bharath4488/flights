# Generated by Django 3.1.4 on 2021-02-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0014_auto_20210207_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_querie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=250)),
                ('messsage', models.TextField(max_length=10000)),
            ],
        ),
    ]
