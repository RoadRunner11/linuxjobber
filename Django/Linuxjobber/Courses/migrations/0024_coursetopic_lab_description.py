# Generated by Django 2.0.1 on 2018-12-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0023_auto_20181217_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetopic',
            name='lab_description',
            field=models.TextField(null=True),
        ),
    ]
