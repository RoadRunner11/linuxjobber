# Generated by Django 2.0.7 on 2019-09-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0067_auto_20190920_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='interest',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
