# Generated by Django 3.1.7 on 2021-11-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20211118_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='gender',
            field=models.CharField(default='Female', max_length=20),
        ),
    ]
