# Generated by Django 2.0.7 on 2019-02-16 21:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_wetask_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
