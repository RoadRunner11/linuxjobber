# Generated by Django 2.0.1 on 2018-11-27 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_merge_20181123_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=20)),
                ('longtitude', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
