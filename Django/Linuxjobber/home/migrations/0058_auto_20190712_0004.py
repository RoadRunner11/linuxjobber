# Generated by Django 2.0.7 on 2019-07-11 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupclass',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='groupclass',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]
