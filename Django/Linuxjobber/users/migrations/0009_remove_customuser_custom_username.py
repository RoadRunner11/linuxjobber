# Generated by Django 2.0.7 on 2019-09-10 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_custom_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='custom_username',
        ),
    ]
