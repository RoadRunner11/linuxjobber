# Generated by Django 2.0.7 on 2019-01-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20190128_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='timestamp',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
