# Generated by Django 2.2.7 on 2020-03-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_currecy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='currecy',
        ),
        migrations.AddField(
            model_name='profile',
            name='money',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
