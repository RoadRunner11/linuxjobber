# Generated by Django 2.0.7 on 2019-12-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0015_auto_20190310_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_id', models.CharField(max_length=255)),
            ],
        ),
    ]
