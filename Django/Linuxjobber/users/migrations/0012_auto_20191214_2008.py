# Generated by Django 2.0.7 on 2019-12-14 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20191213_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_role',
            new_name='available_roles',
        ),
    ]
