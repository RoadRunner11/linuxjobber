# Generated by Django 2.0.8 on 2018-11-11 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_remove_djangostudentrole_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='djangostudentrole',
            name='user',
        ),
        migrations.RemoveField(
            model_name='djangostudent',
            name='role',
        ),
        migrations.DeleteModel(
            name='DjangoStudentRole',
        ),
    ]
