# Generated by Django 2.0.7 on 2019-10-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0074_auto_20191003_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='is_wefaq',
            field=models.BooleanField(default=False),
        ),
    ]
