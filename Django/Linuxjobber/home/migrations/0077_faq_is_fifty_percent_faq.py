# Generated by Django 2.0.7 on 2019-10-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0076_auto_20191004_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='is_fifty_percent_faq',
            field=models.BooleanField(default=False),
        ),
    ]
