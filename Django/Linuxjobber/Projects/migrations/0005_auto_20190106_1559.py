# Generated by Django 2.1.2 on 2019-01-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0004_auto_20190104_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcoursetopic',
            name='topic_title',
            field=models.CharField(max_length=200),
        ),
    ]
