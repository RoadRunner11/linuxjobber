# Generated by Django 2.0.7 on 2020-01-21 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0112_itpartnership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itpartnership',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
