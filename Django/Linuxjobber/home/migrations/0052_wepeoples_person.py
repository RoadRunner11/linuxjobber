# Generated by Django 2.0.7 on 2019-04-11 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_auto_20190411_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='wepeoples',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.werole'),
        ),
    ]