# Generated by Django 2.0.7 on 2019-05-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_userorder_paid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='order_id',
            field=models.CharField(max_length=100),
        ),
    ]
