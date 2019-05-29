# Generated by Django 2.0.7 on 2019-05-10 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0053_auto_20190422_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.CharField(max_length=50)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('latitude', models.CharField(blank=True, max_length=20)),
                ('longtitude', models.CharField(blank=True, max_length=20)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userorder',
            name='order_id',
            field=models.CharField(max_length=200),
        ),
    ]
