# Generated by Django 2.0.7 on 2019-02-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_merge_20190130_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='wework',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
