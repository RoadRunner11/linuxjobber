# Generated by Django 2.2.2 on 2019-12-08 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0088_workexpeligibility_workexpisa_workexppay'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexpeligibility',
            name='expiry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
