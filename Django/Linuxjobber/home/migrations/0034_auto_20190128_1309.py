# Generated by Django 2.0.7 on 2019-01-28 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20190128_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wepeoples',
            name='types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.wetype'),
        ),
    ]
