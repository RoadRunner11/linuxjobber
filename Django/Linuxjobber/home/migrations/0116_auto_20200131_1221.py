# Generated by Django 2.0.7 on 2020-01-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0115_merge_20200129_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itpartnership',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]
